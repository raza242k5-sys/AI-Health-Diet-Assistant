import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(".env"))

API_KEY = os.getenv("OPENROUTER_API_KEY")


def ask_health_question(question, user_data):

    if not API_KEY:
        return "API Key is not loading from .env"

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 🔥 PERSONALIZED PROMPT
    prompt = f"""
You are a professional AI doctor and nutritionist.

User Profile:
- Age: {user_data['age']}
- Gender: {user_data['gender']}
- BMI: {user_data['bmi']}
- Category: {user_data['category']}
- Daily Calories: {user_data['calories']}
- Goal: {user_data['goal']}
- Diet Type: {user_data['diet_type']}
- Workout: {user_data['gym']}
- Disease: {user_data['disease']}

User Question:
{question}

Give a personalized, practical, and easy-to-follow answer.
"""

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful health assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            return f"API Error: {result}"

    except Exception as e:
        return f"Error: {str(e)}"