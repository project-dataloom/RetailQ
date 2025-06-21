import openai
import os

openai.api_key = os.getenv("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")

def ask_llm(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Error: {e}"
