import os
import requests

from dotenv import load_dotenv
from app.tools.calculator import (
    calculate_expression
)

from app.tools.current_time import (
    get_current_time
)

from app.tools.wikipedia_tool import (
    search_wikipedia
)

from app.tools.weather import (
    get_weather
)

from app.tools.web_search import (
    search_web
)

# Load environment variables
load_dotenv()


def generate_ai_response(
    question: str,
    system_prompt: str,
    temperature: float
):
    
    
    # Detect time requests
    if "time" in question.lower():

        # Call time tool
        return get_current_time()

    # Detect calculation requests
    if "calculate" in question.lower():

        # Extract math expression
        expression = question.lower().replace(
            "calculate",
            ""
        ).strip()

        # Call calculator tool
        result = calculate_expression(
            expression
        )

        return result
    
    # Detect Wikipedia search requests
    if "who is" in question.lower():

        # Extract topic
        topic = question.lower().replace(
            "who is",
            ""
        ).strip()

        # Call Wikipedia tool
        return search_wikipedia(topic)
    
    # Detect weather requests
    if "weather" in question.lower():

        # Extract city name
        city = question.lower().replace(
            "weather in",
            ""
        ).strip()

        # Call weather tool
        return get_weather(city)
    
    # Detect web search requests
    if "search" in question.lower():

        # Extract search query
        query = question.lower().replace(
            "search",
            ""
        ).strip()

        # Call web search tool
        results = search_web(query)

        return results

    # Default AI response
    return f"""
    AI Response:

    Question:
    {question}

    System Prompt:
    {system_prompt}

    Temperature:
    {temperature}
    """