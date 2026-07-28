import os
import requests
from config import AI_MODEL

API_URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_openrouter(message: str):

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "model":AI_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ]
        },
        timeout=30
    )

    print(response.status_code)
    print(response.text)

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
