import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
load_dotenv(dotenv_path=Path(".env"))

API_KEY = os.getenv("OPENROUTER_API_KEY")


def ask_health_question(question):

    # 🔒 Check API key
    if not API_KEY:
        return "⚠ API key not found. Please check your .env file."

    # 🔒 Check empty question
    if not question.strip():
        return "⚠ Please enter a valid health question."

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

    try:
        # ⏳ Timeout added (prevents hanging forever)
        response = requests.post(url, headers=headers, json=data, timeout=15)

        # 🚨 If API returns error status
        response.raise_for_status()

        result = response.json()

        # ✅ Check proper structure
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return "⚠ Unexpected API response format."

    except requests.exceptions.Timeout:
        return "⚠ Request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return "⚠ Internet connection error."

    except requests.exceptions.HTTPError as e:
        return f"⚠ API returned an error: {str(e)}"

    except Exception as e:
        return f"⚠ Something went wrong: {str(e)}"