import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(".env"))

API_KEY = os.getenv("OPENROUTER_API_KEY")

def ask_health_question(question):

    if not API_KEY:
        return "API Key is not loading from .env"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a professional AI health assistant."},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"API Error: {result}"