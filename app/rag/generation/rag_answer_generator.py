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


def generate_rag_answer(

    question,
    context
):

    try:

        prompt = f"""

        Answer the question ONLY
        from the given context.

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