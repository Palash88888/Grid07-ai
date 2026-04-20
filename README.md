# Grid07 AI Cognitive System

## Overview
Implements:
- Phase 1: Vector similarity routing (ChromaDB)
- Phase 2: LangGraph pipeline
- Phase 3: RAG-based defense

---

## LangGraph Nodes
LangGraph Node Structure (Brief Overview)

The system is built using a modular LangGraph pipeline designed for controlled and explainable reasoning. The main nodes are:

1. Input Node
Receives the user query.
Performs basic preprocessing and normalization.
2. Query Classifier / Router Node
Determines the intent of the query (medical, general, research, or unsafe).
Routes the query to the appropriate processing path.
3. Retriever Node (RAG Layer)
Fetches relevant context from external knowledge sources (vector database / APIs).
Ensures responses are grounded in real data.
4. Generator Node (LLM)
Uses retrieved context + query to generate a structured response.
Ensures coherent and context-aware output.
5. Post-Processing Node
Formats the response into structured sections (e.g., summary, insights, references).
Removes redundancy and improves readability.
6. Output Node
Sends final response to the user interface.
Prompt Injection Defense Strategy (Phase 3)

To protect the system from prompt injection attacks, multiple layered defenses were implemented:

1. Input Sanitization
User inputs are cleaned and checked for malicious patterns like:
“ignore previous instructions”
system prompt overrides
hidden instruction attempts
2. Instruction Hierarchy Enforcement
System prompts are locked with higher priority than user prompts.
Model is explicitly instructed to never override system rules.
3. Query Classification Filter
Queries are classified before reaching the LLM.
Suspicious or irrelevant instructions are blocked or redirected.
4. Context Isolation
Retrieved documents are treated as untrusted data.
They are never allowed to override system instructions.
5. Output Validation Layer
Final responses are checked for:
leaked system prompts
unsafe instructions
injection artifacts**

---

## Prompt Injection Defense
- System rules override user input  
- Ignore malicious instructions  
- Maintain persona strictly  

---

## Run

uvicorn app.main:app --reload

Demo:
python run_demo.py
