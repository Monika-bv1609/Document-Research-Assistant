import os
import requests

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def generate_ai_response(
    question: str,
    system_prompt: str,
    temperature: float
):

    try:

        response = requests.post(

            "https://api.aimlapi.com/v1/chat/completions",

            headers={

                # API authentication
                "Authorization": (
                    f"Bearer {os.getenv('OPENAI_API_KEY')}"
                ),

                "Content-Type": "application/json"
            },

            json={

                # AI model
                "model": "openai/gpt-4.1-mini",

                # AI conversation messages
                "messages": [

                    {
                        "role": "system",
                        "content": system_prompt
                    },

                    {
                        "role": "user",
                        "content": question
                    }
                ],

                # Controls creativity
                "temperature": temperature,

                # Response size limit
                "max_tokens": 512
            }
        )

        # Convert response to JSON
        data = response.json()

        # Extract AI response
        return data["choices"][0]["message"]["content"]

    except Exception as e:

        print(response.text)

        print(e)

        return "AI request failed."