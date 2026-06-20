import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class GroqService:

    @staticmethod
    def generate_answer(question, documents):

        context = "\n\n".join(documents)

        prompt = f"""
You are an AI assistant that answers ONLY from the uploaded document.

If the answer is not present in the context,
reply exactly:

"I could not find this information in the uploaded document."

Context:

{context}

Question:

{question}

Answer:
"""

        chat_completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            max_tokens=512

        )

        return chat_completion.choices[0].message.content