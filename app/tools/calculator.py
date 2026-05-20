# Simple calculator tool

def calculate_expression(
    expression: str
):

    try:

        # Evaluate math expression
        result = eval(expression)

        return f"Result: {result}"

    except Exception:

        return "Invalid calculation."