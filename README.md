# NavaDisha AI
"A New Direction, Powered by AI" - Empowering Rural India with Legal Knowledge

## Problem Statement
Millions of rural Indians face legal problems daily - landlord disputes, workplace exploitation, domestic issues - but cannot afford lawyers and don't know their basic rights. Legal illiteracy traps them in helplessness.

## Our Solution
NavaDisha AI is a locally deployed AI-powered legal aid assistant that:
--> Understands legal problems described in simple language
--> Explains constitutional rights in easy words
--> Identifies relevant government schemes and helplines
--> Provides immediate actionable steps
--> Logs all queries for legal trend analysis

## SDG Alignment
|              SDG            |            How We Address It                 |
|-----------------------------|----------------------------------------------|
|  SDG 16 - Peace & Justice   | Making legal aid accessible to all citizens  |
|SDG 10 - Reduced Inequalities|     Bridging justice gap for rural poor      |
|     SDG 1 - No Poverty      |  Protecting poor from financial exploitation |

## Track
Track 06 - Open Innovation(UN Sustainable Development Goals)
Tier 2 - Pillar 1 (Web Platform) + Pillar 3 (Local AI Model)

## Why Local AI (Ollama)?
--> Works completely offline
--> No external API calls
--> Data never leaves the device
--> Valid Pillar 3 custom AI implementation
--> Deployable in rural areas with no internet

## Tech Stack
|   Layer  |      Technology      |       Purpose       |
|----------|----------------------|---------------------|
|Frontend  |HTML, CSS, JavaScript |User Interface       |
|Backend   |Python, Flask         |Web Framework        |
|AI Model  |Llama 3.2 3b by Meta  |Legal Intelligence   |
|AI Runtime|Ollama(Local)         |Offline AI Deployment|
|Database  |MySQL                 |Query Logging        |
|Voice     |Web Speech            |Voice Input          |

## Features Completed - Push 1
--> Flask backend running and responding
--> Local Gemma 2B AI connected via Ollama
--> Homepage with legal problem input form
--> Voice input in Bengali, Hindi and English
--> Result page with structured AI legal advice
--> MySQL database logging all queries
--> Fallback response if AI fails
--> SDG 16 aligned prompt engineering

## Features Coming
--> Complaint letter download 
--> Mobile responsive polish
--> Case history page

## Team
|      Member    |                Role               |
|----------------|-----------------------------------|
|Bristi Chowdhury|Backend & AI Integration           |
|Adrika Sarkar   |Frontend Templates(HTML,CSS,JS)    |
|Moupiya Aich    |RAG Pipeline, database & Legal Data|

## How to Run
bash
pip install flask ollama mysql-connector-python python-docx langchain langchain-community chromadb sentence-transformers pypdf rank_bm25 python-dotenv
ollama pull llama3.1
python ingest.py
python app.py

Open browser --> http://127.0.0.1:5000

Note: Llama 3.1 8B runs completely locally on CPU. Response time is 2-5 minutes — intentional for offline rural deployment with no internet dependency.

## Impact
-->40M+ pending legal cases in India
-->70% rural citizens unaware of rights
-->300M+ people who couldn't benefit
-->0 rupees cost to end user

## Privacy
AI runs locally - user data never leaves their device
No external API calls. Complete data privacy guaranteed.
