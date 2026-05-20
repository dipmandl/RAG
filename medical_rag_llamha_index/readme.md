#  Medical RAG System (LlamaIndex + HuggingFace + Ollama)

A fully local Retrieval-Augmented Generation (RAG) application for answering medical questions using:

-  LlamaIndex
-  HuggingFace Embeddings
-  Ollama (Llama 3)
-  Local Vector Storage

This project allows users to ask medical-related questions from their own documents without using OpenAI APIs.

---

#  Features

-  Load PDFs and text documents
-  Semantic search using vector embeddings
-  Local LLM responses using Ollama
-  Persistent vector index storage
-  Fully offline after setup
-  Improved chunking and retrieval
-  Better response generation using `tree_summarize`

---

#  Tech Stack

| Component | Technology |
|---|---|
| Framework | LlamaIndex |
| Embeddings | HuggingFace |
| Embedding Model | `BAAI/bge-small-en-v1.5` |
| LLM | Ollama (`llama3`) |
| Language | Python |
| Storage | Local persistent storage |

---

#  Project Structure

```text
medical_rag_llama_index/
│
├── data/                  # Input PDFs / text documents
├── storage/               # Auto-generated vector index
├── ingest.py              # Build vector index
├── query.py               # Query chatbot
├── requirements.txt       # Project dependencies
├── README.md
⚙️ Installation
1️Clone Repository
git clone <your-repo-url>
cd medical_rag_llama_index
2️ Create Virtual Environment (Recommended)
Windows
python -m venv venv
venv\Scripts\activate
3️Install Dependencies
pip install -r requirements.txt
🦙 Install Ollama

Download and install Ollama:

 https://ollama.com/download

Pull Llama 3 Model
ollama pull llama3
 Add Your Documents

Place your PDFs or text files inside:

data/
Build Vector Index

Run:

python ingest.py

This will:

load documents
split text into chunks
generate embeddings
store vector index in storage/
Start Medical Chatbot

Run:

python query.py

Example:

Ask Medical Question: What are symptoms of diabetes?
Example Questions
What tests diagnose diabetes?
Explain hypertension treatment.
What are side effects of paracetamol?
What is an MRI scan used for?
Explain blood sugar levels.


sample output:

PS C:\Users\DipakMandlik\Desktop\medical_rag_llamha_index> python .\query.py                  
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|█████████████████████████████████████████████████████████████████████████████████| 199/199 [00:00<00:00, 8320.95it/s]

Medical RAG Chatbot Ready (type 'exit' to quit)

Ask Medical Question: DIABETES TESTS

Answer:
 The tests_info.pdf file contains information about various tests related to medical rag llamha index. Among these tests, there might be some that are used for detecting or monitoring diabetes. Some possible diabetes-related tests mentioned in the file could include:

1. Hemoglobin A1c (HbA1c) test: This test measures the average blood sugar levels over the past 2-3 months.
2. Fasting plasma glucose (FPG) test: This test measures the blood glucose level after an overnight fast.
3. Oral glucose tolerance test (OGTT): This test measures how well the body regulates blood sugar levels in response to consuming a sugary drink.

These tests might be used to diagnose, monitor, or manage diabetes. However, it's essential to note that this is not an exhaustive list and more comprehensive information should be consulted for a definitive answer.

--------------------------------------------------