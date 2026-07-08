import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question_or_prompt, retrieved_chunks=None):

    if retrieved_chunks:
        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
You are a helpful AI document assistant.

Answer ONLY using the provided context.

If the answer is not available in the context, say:
"The provided documents do not contain enough information."

Context:
{context}

Question:
{question_or_prompt}

Answer:
"""
    else:
        prompt = question_or_prompt

    response = model.generate_content(prompt)

    return response.text