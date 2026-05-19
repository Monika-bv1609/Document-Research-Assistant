from app.tools.calculator import (
    calculate_expression
)

from app.tools.current_time import (
    get_current_time
)

from app.tools.weather import (
    get_weather
)

from app.tools.web_search import (
    search_web
)

from app.services.tool_router import (
    choose_tool
)


def generate_ai_response(
    question: str,
    system_prompt: str,
    temperature: float
):

    # Choose appropriate tool
    decision = choose_tool(question)

    tool = decision["tool"]

    reason = decision["reason"]

    print(f"Selected Tool: {tool}")

    print(f"Reason: {reason}")

    # Calculator workflow
    if tool == "calculator":

        expression = (
            question
            .replace("calculate", "")
            .strip()
        )

        return calculate_expression(
            expression
        )

    # Time workflow
    elif tool == "time":

        return get_current_time()

    # Weather workflow
    elif tool == "weather":

        city = (
            question
            .replace("weather in", "")
            .strip()
        )

        return get_weather(city)

    # Web search workflow
    elif tool == "web_search":

        return search_web(question)

    # Default AI response
    return f"""
    AI Response

    Question:
    {question}

    System Prompt:
    {system_prompt}

    Temperature:
    {temperature}
    """