from app.services.tool_router import (
    choose_tool
)


def create_execution_plan(
    question: str
):

    question = question.lower()

    plan = []

    # AI decides primary tool
    tool = choose_tool(
        question
    )

    print(
        "AI SELECTED TOOL:",
        tool
    )

    # Dynamic planning

    if tool == "web_search":

        plan.append(
            "web_search"
        )

        # If research/summarize needed
        if (

            "summarize" in question

            or

            "research" in question
        ):

            plan.append(
                "summarize"
            )

    elif tool == "weather":

        plan.append(
            "weather"
        )

        if "summarize" in question:

            plan.append(
                "summarize"
            )

    elif tool == "calculator":

        plan.append(
            "calculator"
        )

    elif tool == "time":

        plan.append(
            "time"
        )

    else:

        plan.append(
            "general"
        )

    print(
        "EXECUTION PLAN:",
        plan
    )

    return plan