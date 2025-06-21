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
