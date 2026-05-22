from sklearn.metrics.pairwise import (
    cosine_similarity
)

from app.rag.retrieval.embedding_generator import (
    model
)


def semantic_search(

    query: str,
    chunks: list,
    chunk_embeddings,
    top_k: int = 3
):

    # Convert query to embedding
    query_embedding = model.encode(
        [query]
    )

    # Calculate similarities
    similarities = cosine_similarity(

        query_embedding,
        chunk_embeddings
    )[0]

    # Get top matching indices
    top_indices = similarities.argsort()[
        -top_k:
    ][::-1]

    relevant_chunks = []

    for index in top_indices:

        print(
            "MATCH SCORE:",
            similarities[index]
        )

        relevant_chunks.append(
            chunks[index]
        )

    return relevant_chunks