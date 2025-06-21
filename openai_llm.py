import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

# Load from env or secrets.toml
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_PROJECT_ID = os.getenv("OPENAI_PROJECT_ID")  # Optional but good practice

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(prompt: str) -> str:
    try:
        messages: list[ChatCompletionMessageParam] = [
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM error: {str(e)}"
