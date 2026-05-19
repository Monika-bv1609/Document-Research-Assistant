import requests
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenRouter API key
API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

# OpenRouter endpoint
BASE_URL = (
    "https://openrouter.ai/api/v1/chat/completions"
)


def choose_tool(
    question: str
):

    try:

        # Debug API key
        print("API KEY:", API_KEY)

        # Router prompt
        router_prompt = f"""
        You are an AI tool router.

        Available tools:

        1. calculator
        → For math calculations

        2. weather
        → For weather information

        3. time
        → For current time requests

        4. web_search
        → For latest news or internet searches

        5. general
        → For normal conversation

        ONLY return the tool name.

        User Question:
        {question}
        """

        # Send request
        response = requests.post(

            BASE_URL,

            headers={

                "Authorization":
                f"Bearer {API_KEY}",

                "Content-Type":
                "application/json"
            },

            json={

                "model":
                "deepseek/deepseek-r1-0528-qwen3-8b:free",

                "messages": [

                    {
                        "role": "system",
                        "content":
                        "You are a tool routing AI."
                    },

                    {
                        "role": "user",
                        "content":
                        router_prompt
                    }
                ],

                "temperature": 0
            }
        )

        # Debug response status
        print("STATUS CODE:", response.status_code)

        # Convert to JSON
        data = response.json()

        print("RESPONSE:", data)

        # Check for errors
        if "choices" not in data:

            print(
                "LLM routing failed."
            )

            print(
                "Falling back to keyword router."
            )

            # Fallback routing
            question_lower = question.lower()

            if any(word in question_lower for word in [

                "calculate",
                "multiply",
                "add",
                "subtract",
                "*",
                "+",
                "-",
                "/"
            ]):

                return "calculator"

            elif "weather" in question_lower:

                return "weather"

            elif "time" in question_lower:

                return "time"

            elif any(word in question_lower for word in [

                "search",
                "latest",
                "news"
            ]):

                return "web_search"

            return "general"

        # Extract tool
        tool = data["choices"][0][
            "message"
        ]["content"].strip()

        print(
            "LLM Selected Tool:",
            tool
        )

        return tool

    except Exception as e:

        print("ERROR:", e)

        return "general"