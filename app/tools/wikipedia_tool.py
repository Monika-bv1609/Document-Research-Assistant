import wikipedia


def search_wikipedia(
    query: str
):

    try:

        # Search matching pages
        search_results = wikipedia.search(
            query
        )

        # No results found
        if not search_results:

            return (
                "No Wikipedia results found."
            )

        # Take first matching result
        topic = search_results[0]

        # Fetch summary
        result = wikipedia.summary(
            topic,
            sentences=2
        )

        return result

    except Exception as e:

        print(e)

        return (
            "Wikipedia information not found."
        )