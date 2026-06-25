def retrieve_relevant_chunks(

    query: str,
    chunks: list
):

    best_chunk = ""

    best_score = 0

    # Ignore common words
    stop_words = {

        "where",
        "what",
        "does",
        "did",
        "is",
        "the",
        "a",
        "an",
        "in",
        "on",
        "at"
    }

    query_words = [

        word

        for word in query.lower().split()

        if word not in stop_words
    ]


    # Search chunks
    for chunk in chunks:

        chunk_lower = chunk.lower()

        score = 0

        for word in query_words:

            if word in chunk_lower:

                score += 1

        # Keep highest score
        if score > best_score:

            best_score = score

            best_chunk = chunk


    # Return best match
    if best_score > 0:

        return [best_chunk]

    return []