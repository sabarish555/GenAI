import os
import requests

# Get API key from environment
GROQ_API_KEY = "please enter your api key here"
#os.getenv("GROQ_API_KEY")  # You can also load from .env

# Groq endpoint and model
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"

def generate_answer(query, context_chunks):
    """
    Sends query + relevant context to Groq and returns the answer.
    """
    context_text = "\n\n".join(
        [f"Source: {chunk['source']}\nContent: {chunk['text']}" for chunk in context_chunks]
    )

    messages = [
        {"role": "system", "content": "You are an HR policy assistant. Answer based only on the provided context. Cite source PDF and page number."},
        {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion:\n{query}"}
    ]

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.3
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Groq API failed: {response.status_code}\n{response.text}")

    result = response.json()
    return result["choices"][0]["message"]["content"]
