from sklearn.metrics.pairwise import (
    cosine_similarity
)

from app.tools.embedding_generator import (
    model
)


def semantic_search(

    query: str,
    chunks: list,
    chunk_embeddings
):

    # Convert query to embedding
    query_embedding = model.encode(
        [query]
    )

    # Compare similarity
    similarities = cosine_similarity(

        query_embedding,
        chunk_embeddings
    )[0]

    # Best matching chunk index
    best_match_index = (
        similarities.argmax()
    )

    # Best chunk
    best_chunk = chunks[
        best_match_index
    ]

    print(
        "BEST MATCH SCORE:",
        similarities[
            best_match_index
        ]
    )

    return best_chunk