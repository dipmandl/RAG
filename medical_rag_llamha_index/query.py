from llama_index.core import (
    load_index_from_storage,
    PromptTemplate
)

from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.settings import Settings

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# =========================================================
# Embedding Model (MUST match ingest.py)
# =========================================================

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# =========================================================
# Local LLM using Ollama
# =========================================================

Settings.llm = Ollama(
    model="llama3",
    request_timeout=120.0
)

# =========================================================
# Custom Medical Prompt
# =========================================================

qa_prompt = PromptTemplate(
    """
You are an intelligent medical AI assistant.

Use ONLY the provided medical context to answer the question.

---------------------
Context:
{context_str}
---------------------

Question:
{query_str}

Instructions:
- Give clear and medically accurate answers.
- Keep responses structured and concise.
- Use bullet points when useful.
- Do not make up information.
- If answer is not available in context, say:
  "I could not find this information in the provided medical documents, but in case some relevant information found 
  give in that way I could find the relevant information please be carefull and assist with doctor before proceeding."

Answer:
"""
)

# =========================================================
# Load Stored Index
# =========================================================

storage_context = StorageContext.from_defaults(
    persist_dir="./storage"
)

index = load_index_from_storage(storage_context)

# =========================================================
# Query Engine
# =========================================================

query_engine = index.as_query_engine(
    similarity_top_k=5,
    response_mode="tree_summarize",
    text_qa_template=qa_prompt
)

# =========================================================
# Chat Loop
# =========================================================

print("\n Medical RAG Chatbot Ready")
print("Type 'exit' to quit.\n")

while True:

    question = input("Ask Medical Question: ")

    if question.lower() == "exit":
        print("\nGoodbye ")
        break

    response = query_engine.query(question)

    print("\n Answer:\n")
    print(response)
    print("\n" + "=" * 70)