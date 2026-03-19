import requests
import json

GROQ_API_KEY = "YOUR_GROQ_API_KEY"

def score_lead(lead):
    prompt = f"""
    Score this profile (0–100):
    Bio: {lead['bio']}
    Followers: {lead['followers']}
    Engagement: {lead['engagement']}

    Return JSON: {{ "score": number, "reason": "text" }}
    """

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    try:
        content = response.json()["choices"][0]["message"]["content"]
        return json.loads(content)
    except:
        return {"score": 0, "reason": "error"}
