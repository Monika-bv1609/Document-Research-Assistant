def choose_tool(
    question: str
):

    question = question.lower()

    # Simulated AI reasoning

    calculator_words = [

        "calculate",
        "multiply",
        "add",
        "subtract",
        "*",
        "+",
        "-",
        "/"
    ]

    search_words = [

        "search",
        "latest",
        "news"
    ]

    # AI-like decision making
    if any(word in question for word in calculator_words):

        return {
            "tool": "calculator",
            "reason":
            "Math operation detected"
        }

    elif "weather" in question:

        return {
            "tool": "weather",
            "reason":
            "Weather information requested"
        }

    elif "time" in question:

        return {
            "tool": "time",
            "reason":
            "Current time requested"
        }

    elif any(word in question for word in search_words):

        return {
            "tool": "web_search",
            "reason":
            "Web search intent detected"
        }

    return {
        "tool": "general",
        "reason":
        "General conversation"
    }