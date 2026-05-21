import requests


def generate_rag_answer(

    question: str,
    context: str
):

    try:

        prompt = f"""
        Answer the question ONLY
        using the provided context.

        Context:
        {context}

        Question:
        {question}

        Give a short and clear answer.
        """

        response = requests.post(

            "http://localhost:11434/api/generate",

            json={

                "model":
                "llama3.2",

                "prompt":
                prompt,

                "stream":
                False
            }
        )

        data = response.json()

        print(data)

        answer = data.get(

            "response",

            "No response generated."
        )

        return answer

    except Exception as e:

        print(e)

        return (
            "Answer generation failed."
        )