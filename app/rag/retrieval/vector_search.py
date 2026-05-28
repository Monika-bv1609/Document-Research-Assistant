from app.rag.retrieval.embedding_generator import (
    generate_embeddings
)

from app.rag.vectorstore.vector_store import (
    VectorStore
)


def semantic_search(question):

    # Generate question embedding
    question_embedding = generate_embeddings(
        [question]
    )[0]

    # Search in ChromaDB
    results = VectorStore.search(

        query_embedding=question_embedding,

        top_k=3
    )

    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    final_results = []

    for doc, metadata in zip(

        documents,

        metadatas
    ):

        final_results.append({

            "chunk": doc,

            "metadata": metadata
        })

    return final_results