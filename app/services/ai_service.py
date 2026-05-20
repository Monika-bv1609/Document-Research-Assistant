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

from app.agents.research_agent import (
    research_ai_topic
)

from app.agents.planner_agent import (
    create_execution_plan
)

from app.agents.executor_agent import (
    execute_plan
)

def generate_ai_response(
    question: str,
    system_prompt: str,
    temperature: float
):

    # Generate execution plan
    plan = create_execution_plan(
        question
    )

    # Execute dynamic plan
    return execute_plan(
        plan,
        question
    )
    

    # Execute research workflow
    if (


        "summarize" in plan
    ):

        return research_ai_topic(
            question
        )

    # Single tool routing
    tool = choose_tool(
        question
    )

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

    # Default response
    return f"""

AI Response

Question:
{question}

System Prompt:
{system_prompt}

Temperature:
{temperature}

"""