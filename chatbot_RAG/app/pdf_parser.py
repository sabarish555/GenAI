import os
import fitz
import hashlib

def get_all_pdfs(folder="data"):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.pdf')]
def hash_chunk(text):
    return hashlib.md5(text.strip().encode("utf-8")).hexdigest()

def parse_pdf(filepath, chunk_size=500, chunk_overlap=50):
    doc = fitz.open(filepath)
    chunks = []
    seen_hashes = set()

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        words = text.split()
        i = 0

        while i < len(words):
            chunk_words = words[i:i+chunk_size]
            chunk_text = " ".join(chunk_words)
            i += chunk_size - chunk_overlap

            chunk_hash = hash_chunk(chunk_text)
            if chunk_hash in seen_hashes or len(chunk_text.strip()) < 10:
                continue

            chunks.append({
                "text": chunk_text,
                "source": os.path.basename(filepath),
                "page": page_num,
                "hash": chunk_hash
            })
            seen_hashes.add(chunk_hash)

    return chunks

print("pdf parser loaded")