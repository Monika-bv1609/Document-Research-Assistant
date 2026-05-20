from app.tools.tool_registry import (
    TOOLS
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

            tool_function = TOOLS[
                "web_search"
            ]

            results = tool_function(
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

        # Dynamic tool execution
        elif step in TOOLS:

            tool_function = TOOLS[
                step
            ]

            # Weather tool
            if step == "weather":

                city = (
                    question
                    .replace(
                        "weather in",
                        ""
                    )
                    .strip()
                )

                result = tool_function(
                    city
                )

            # Calculator tool
            elif step == "calculator":

                expression = (
                    question
                    .replace(
                        "calculate",
                        ""
                    )
                    .strip()
                )

                result = tool_function(
                    expression
                )

            # Time tool
            elif step == "time":

                result = tool_function()

            # Other tools
            else:

                result = tool_function(
                    question
                )

            context[
                "final_response"
            ] = result

    return context.get(
        "final_response",
        "Execution failed."
    )