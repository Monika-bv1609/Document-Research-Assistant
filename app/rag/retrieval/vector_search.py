from app.rag.retrieval.embedding_generator import (
    generate_embeddings
)

from app.rag.vectorstore.vector_store import (
    VectorStore
)

from langsmith import traceable


@traceable(name="semantic_search")
def semantic_search(question, policy_type=None):

    # Generate query embedding
    question_embedding = generate_embeddings(
        [question]
    )[0]

    # Retrieve Top-K candidate chunks
    results = VectorStore.search(
        query_embedding=question_embedding,
        top_k=10,
        policy_type=policy_type
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

    print(f"\n[VECTOR SEARCH] Retrieved {len(final_results)} chunks")

    for result in final_results:

        print(result["metadata"])

    return final_results