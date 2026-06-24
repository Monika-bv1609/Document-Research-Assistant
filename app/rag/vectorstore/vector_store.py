from app.rag.vectorstore.chroma_client import collection


class VectorStore:

    @staticmethod
    def add_documents(

        chunks,

        embeddings,

        metadata_list,

        ids
    ):

        collection.add(

            documents=chunks,

            embeddings=embeddings,

            metadatas=metadata_list,

            ids=ids
        )

    @staticmethod
    def search(

        query_embedding,

        top_k=5,
        
        policy_type=None
    ):

        print(
            f"[CHROMA FILTER] policy_type={policy_type}"
        )
        results = collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k
        )

        # Filter results by policy type if specified
        if policy_type:

            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
                where={
                    "policy_type": policy_type
                }
            )

        else:

            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )

        return results

    @staticmethod
    def document_exists(filename):

        results = collection.get()

        print("========== STORED METADATA ==========")

        for item in results["metadatas"][:5]:
            print(item)

        print("====================================")

        metadatas = results.get(
            "metadatas",
            []
        )

        for metadata in metadatas:

            if metadata["source"] == filename:

                return True

        return False
    


    @staticmethod
    def debug_metadata():

        results = collection.get()

        print("\n========== CHROMA METADATA ==========")

        for metadata in results["metadatas"][:20]:

            print(metadata)

        print("====================================\n")