# ⚖️ NavaDisha AI
> *"A New Direction, Powered by AI"* — Empowering Rural India with Legal Knowledge

---

## Problem Statement

Millions of rural Indians face legal problems daily — landlord disputes, workplace exploitation, domestic violence, caste discrimination — but cannot afford lawyers and don't know their basic rights. Legal illiteracy traps them in helplessness.

---

## Our Solution

NavaDisha AI is a **locally deployed AI-powered legal aid assistant** that:

- Understands legal problems described in simple language (Bengali, Hindi, English)
- Explains constitutional rights in easy words
- Identifies relevant government schemes, laws, and helplines
- Provides immediate actionable steps
- Supports voice input with auto language detection
- Logs all queries anonymously for legal trend analysis via a government dashboard

---

## SDG Alignment
 
|             SDG               |               How We Address It                 |
|-------------------------------|-------------------------------------------------|
| SDG 16 — Peace & Justice      | Making legal aid accessible to all citizens     |
| SDG 10 — Reduced Inequalities | Bridging the justice gap for rural poor         |
| SDG 1 — No Poverty            | Protecting the poor from financial exploitation |

---

## Track

**Track 06 — Open Innovation (UN Sustainable Development Goals)**  
Tier 2 — Pillar 1 (Web Platform) + Pillar 3 (Local AI Model)

---

## Why Local AI (Ollama)?

- Works completely offline
- No external API calls
- Data never leaves the device
- Valid Pillar 3 custom AI implementation
- Deployable in rural areas with no internet

---

## Tech Stack

|   Layer    |         Technology           |          Purpose          |
|------------|------------------------------|---------------------------|
| Frontend   | HTML, CSS, JavaScript        | User Interface            |
| Backend    | Python, Flask                | Web Framework             |
| AI Model   | Llama 3.2 3B by Meta         | Legal Intelligence        |
| AI Runtime | Ollama (Local)               | Offline AI Deployment     |
| RAG        | LangChain + ChromaDB + BM25  | Hybrid Retrieval Pipeline |
| Embeddings | HuggingFace all-MiniLM-L6-v2 | Semantic Search           |
| Database   | MySQL                        | Query Logging & Analytics |
| Voice      | Web Speech API               | Multilingual Voice Input  |

---

# Features Completed

- Flask backend running and responding
- Local Llama 3.2 3B AI connected via Ollama with Hybrid RAG pipeline (ChromaDB dense + BM25 sparse, 50/50)
- Homepage with legal problem input form
- Voice input in Bengali, Hindi, and English with auto language detection
- State selector for regional tracking
- Result page with structured AI legal advice
- MySQL database logging all queries with auto-tagged legal category and region
- Government dashboard at `/dashboard` showing legal query trends by state and category
- Fallback response if query is off-topic
- Session timeout with inactivity redirect
- Loading overlay while AI processes query
- SDG 16 aligned prompt engineering

---

## Features Coming

- State selection
- Loading page
- Session timout page
- Case history page (expanded)

---

## Team

|      Member      |                Role                 |
|------------------|-------------------------------------|
| Bristi Chowdhury | Backend & AI Integration            |
| Adrika Sarkar    | Frontend Templates (HTML, CSS, JS)  |
| Moupiya Aich     | RAG Pipeline, Database & Legal Data |

---

## How to Run

```bash
pip install flask ollama mysql-connector-python python-docx langchain langchain-community chromadb sentence-transformers pypdf rank_bm25 python-dotenv
ollama pull llama3.2
python ingest.py
python app.py
```

Open browser → http://127.0.0.1:5000

> **Note:** Llama 3.2 3B runs completely locally on CPU. Response time is 2–5 minutes — intentional for offline rural deployment with no internet dependency.

---

## USP — Case History Dashboard

NavaDisha AI maintains a searchable history of all legal queries submitted — anonymized for privacy. Government officials can use this data to identify the most common legal problems in specific regions, enabling data-driven deployment of legal aid camps and policy interventions.

Access at → http://127.0.0.1:5000/dashboard

---

## Impact

- 40M+ pending legal cases in India
- 70% rural citizens unaware of their rights
- 300M+ people who couldn't benefit from existing legal systems
- **₹0** cost to end user

---

## Privacy

AI runs locally — user data never leaves the device. No external API calls. Complete data privacy guaranteed.
