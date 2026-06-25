from app.tools.tool_registry import (
    TOOLS
)


def execute_plan(
    plan: list,
    question: str
):

    context = {}

    for step in plan:

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

        # Analyze step
        elif step == "analyze":

            summary = context.get(
                "final_response",
                ""
            )

            analysis = f"""

AI Analysis Report

{summary}

Business Insight:
AI adoption is accelerating across
software, healthcare, enterprise,
automation, and research industries.

Trend Analysis:
Companies are increasingly investing
in AI-driven automation and intelligent
workflow systems.

Future Outlook:
Agentic AI and autonomous systems
are becoming major focus areas in
modern software engineering.
"""

            context[
                "final_response"
            ] = analysis

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