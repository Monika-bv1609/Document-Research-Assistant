from app.tools.web_search import (
    search_web
)


def research_ai_topic(
    query: str
):

    try:

        print(
            "STEP 1: Searching web..."
        )

        # Search internet
        results = search_web(query)

        print(
            "STEP 2: Results collected"
        )

        # Extract titles
        titles = []

        for result in results:

            titles.append(
                result.get("title")
            )

        # Build summary
        summary = f"""
Research Summary

Topic:
{query}

Key Findings:

"""

        for index, title in enumerate(
            titles,
            start=1
        ):

            summary += (
                f"{index}. {title}\n"
            )

        summary += """

Overall Trend:
AI industry is rapidly growing with
continuous advancements in AI tools,
research, and enterprise adoption.
"""

        print(
            "STEP 3: Summary generated"
        )

        return summary

    except Exception as e:

        print(e)

        return (
            "Research agent failed."
        )