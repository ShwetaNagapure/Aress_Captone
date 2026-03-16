import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_reply(user_query):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a professional customer support assistant."},
            {"role": "user", "content": user_query}
        ],
        temperature=0.3,
        max_tokens=200
    )

    return response.choices[0].message.content