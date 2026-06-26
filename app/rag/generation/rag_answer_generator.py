from openai import OpenAI
import os

from dotenv import (
    load_dotenv
)

load_dotenv()

client = OpenAI(

    api_key=os.getenv(
        "GROQ_API_KEY"
    ),
    base_url="https://api.groq.com/openai/v1"
)

from langsmith import traceable

@traceable(name="generate_rag_answer")
def generate_rag_answer(

    question,
    context
):

    try:

        prompt = f"""
        You are an AI HR Assistant.

        Answer ONLY using the information available in the provided context.

        Rules:
        - Do NOT use your own knowledge.
        - Do NOT make assumptions.
        - Do NOT guess.
        - If the answer is not present in the context, reply exactly:
        "I couldn't find this information in the uploaded HR policy documents."
        - Keep the answer concise and factual.

        Context:
        {context}

        Question:
        {question}
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0
        )

        answer = (
            response
            .choices[0]
            .message
            .content
        )

        return answer

    except Exception as error:

        print(error)

        return (
            "LLM could not generate answer."
        )