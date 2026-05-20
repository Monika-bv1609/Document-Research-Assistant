from ddgs import DDGS


def search_web(
    query: str
):

    try:

        results = []

        with DDGS() as ddgs:

            search_results = list(

                ddgs.text(
                    query,
                    max_results=3
                )
            )

            # Debugging
            print(search_results)

            for result in search_results:

                results.append({

                    "title": result.get(
                        "title"
                    ),

                    "url": result.get(
                        "href"
                    )
                })

        return results

    except Exception as e:

        print(e)

        return [
            "Web search failed."
        ]