from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Load the same embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load Chroma vector DB
CHROMA_DIR = "vectorstore"
client = chromadb.PersistentClient(path=CHROMA_DIR)

client = chromadb.Client(Settings(
    persist_directory=CHROMA_DIR,
    anonymized_telemetry=False
))
collection = client.get_or_create_collection(name="hr_policies")

def retrieve_relevant_chunks(query, k=4):
    """
    Given a query, returns top-k relevant chunks from vector DB.
    """
    query_embedding = embedder.encode(query).tolist()

    # Perform similarity search in Chroma
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    # Extract matched texts with metadata
    chunks = []
    for doc, metadata in zip(results["documents"][0], results["metadatas"][0]):
        source_info = f"{metadata['source']} (page {metadata['page']})"
        chunks.append({
            "text": doc,
            "source": source_info
        })

    return chunks
print("retriever loaded")