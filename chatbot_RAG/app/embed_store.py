import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Initialize Chroma vector DB
CHROMA_DIR = "vectorstore"

client = chromadb.Client(Settings(
    persist_directory=CHROMA_DIR,
    anonymized_telemetry=False
))

collection = client.get_or_create_collection(name="hr_policies")

# Load local embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # Small and fast

def add_chunks_to_store(chunks):
    existing_ids = set(collection.get()["ids"])

    new_texts, new_ids, new_metadatas = [], [], []

    for chunk in chunks:
        chunk_id = chunk["hash"]
        if chunk_id in existing_ids:
            continue  # Skip duplicates

        new_texts.append(chunk["text"])
        new_ids.append(chunk_id)
        new_metadatas.append({
            "source": chunk["source"],
            "page": chunk["page"]
        })

    if new_texts:
        embeddings = embedder.encode(new_texts).tolist()
        collection.add(
            documents=new_texts,
            embeddings=embeddings,
            metadatas=new_metadatas,
            ids=new_ids
        )
        #client.persist()
        print(f"✅ Added {len(new_texts)} new chunks.")
    else:
        print("ℹ️ No new chunks to add.")
print("embed store loaded")