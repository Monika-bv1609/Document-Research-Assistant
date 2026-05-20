def create_execution_plan(
    question: str
):

    question = question.lower()

    plan = []

    # Research workflow
    if (

        "research" in question

        or

        "summarize" in question
    ):

        plan.append(
            "web_search"
        )

        plan.append(
            "summarize"
        )

    # Weather workflow
    elif "weather" in question:

        plan.append(
            "weather"
        )

    # Time workflow
    elif "time" in question:

        plan.append(
            "time"
        )

    # Calculator workflow
    elif any(word in question for word in [

        "calculate",
        "multiply",
        "add",
        "subtract",
        "*",
        "+",
        "-"
    ]):

        plan.append(
            "calculator"
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