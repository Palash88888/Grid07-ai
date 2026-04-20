# Grid07 AI Cognitive System

## Overview
Implements:
- Phase 1: Vector similarity routing (ChromaDB)
- Phase 2: LangGraph pipeline
- Phase 3: RAG-based defense

---

## LangGraph Nodes
1. Decide → selects topic & query  
2. Search → mock tool  
3. Generate → LLM creates JSON post  

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
