from sklearn.metrics.pairwise import (
    cosine_similarity
)

import numpy as np

from app.rag.retrieval.embedding_generator import (
    generate_embeddings
)


def semantic_search(

    question,

    chunks,

    embeddings,

    metadata
):

    # Generate embedding for question
    question_embedding = (
        generate_embeddings(
            [question]
        )[0]
    )

    # Convert to numpy arrays
    question_embedding = np.array(
        question_embedding
    ).reshape(1, -1)

    embeddings_array = np.array(
        embeddings
    )

    # Compute similarity
    similarities = cosine_similarity(

        question_embedding,

        embeddings_array
    )[0]

    # Get top matching chunk
    top_indices = similarities.argsort()[-3:][::-1]

    results = []

    for idx in top_indices:

        results.append({

            "chunk":
            chunks[idx],

            "metadata":
            metadata[idx]
        })

    return results