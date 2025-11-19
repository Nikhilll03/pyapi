import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
#uri="https://api.openai.com/v1/chat/completions"
uri="https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
payload={
    "model": "gemini-2.5-flash",
    "messages": [
        {"role": "user", "content": "one best software movies name" }
    ]
}
response=requests.post(uri, headers=headers, json=payload)

print(response.json())##["choices"][0]["message"]["content"]###