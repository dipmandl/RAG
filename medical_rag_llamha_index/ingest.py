from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter

# ---- Embeddings ----
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# ---- Better chunking ----
Settings.text_splitter = SentenceSplitter(
    chunk_size=512,
    chunk_overlap=50
)

# ---- Load documents ----
documents = SimpleDirectoryReader("data").load_data()

# ---- Create index ----
index = VectorStoreIndex.from_documents(documents)

# ---- Save index ----
index.storage_context.persist(persist_dir="./storage")

print("Index created and saved successfully.")