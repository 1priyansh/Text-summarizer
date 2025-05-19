import openai
from backend.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_summary(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes notes."},
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ],
        max_tokens=150,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()
