import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
import requests

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

def generate_dm(lead):
    prompt = f"""
    Write a short, human DM.
    Bio: {lead['bio']}
    Post: {lead['recent_post']}
    Max 2 lines.
    """

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
        json={
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return response.json()["choices"][0]["message"]["content"]
