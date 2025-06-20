import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
