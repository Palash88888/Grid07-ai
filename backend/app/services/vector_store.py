from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

personas = [
    ("Bot_A", "AI, crypto, Elon Musk, tech optimism"),
    ("Bot_B", "Anti AI, capitalism critique, privacy, nature"),
    ("Bot_C", "Finance, markets, ROI, trading")
]

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

texts = [p[1] for p in personas]
metadatas = [{"bot_id": p[0]} for p in personas]

VECTOR_DB = Chroma.from_texts(texts, embedding, metadatas=metadatas)


def route_post_to_bots(post_content: str, threshold: float = 0.85):
    results = VECTOR_DB.similarity_search_with_score(post_content, k=3)

    matched = []
    for doc, score in results:
        similarity = 1 - score
        if similarity >= threshold:
            matched.append({
                "bot_id": doc.metadata["bot_id"],
                "similarity": round(similarity, 3)
            })

    return matched
