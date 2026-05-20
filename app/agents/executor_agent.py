from app.tools.web_search import (
    search_web
)

from app.tools.weather import (
    get_weather
)

from app.tools.current_time import (
    get_current_time
)

from app.tools.calculator import (
    calculate_expression
)


def execute_plan(
    plan: list,
    question: str
):

    context = {}

    for step in plan:

        print(
            f"EXECUTING STEP: {step}"
        )

        # Web search step
        if step == "web_search":

            results = search_web(
                question
            )

            context[
                "search_results"
            ] = results

        # Summarization step
        elif step == "summarize":

            search_results = context.get(
                "search_results",
                []
            )

            titles = []

            for result in search_results:

                titles.append(
                    result.get("title")
                )

            summary = (
                "Research Summary\n\n"
            )

            for index, title in enumerate(
                titles,
                start=1
            ):

                summary += (
                    f"{index}. {title}\n"
                )

            summary += """

Overall Trend:
AI adoption and innovation
continue to grow rapidly.
"""

            context[
                "final_response"
            ] = summary

        # Weather step
        elif step == "weather":

            city = (
                question
                .replace("weather in", "")
                .strip()
            )

            weather = get_weather(
                city
            )

            context[
                "final_response"
            ] = weather

        # Time step
        elif step == "time":

            context[
                "final_response"
            ] = get_current_time()

        # Calculator step
        elif step == "calculator":

            expression = (
                question
                .replace("calculate", "")
                .strip()
            )

            result = (
                calculate_expression(
                    expression
                )
            )

            context[
                "final_response"
            ] = result

    return context.get(
        "final_response",
        "Execution failed."
    )