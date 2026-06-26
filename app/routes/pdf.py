from typing import List
from fastapi import Form
from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

from app.config import RERANK_THRESHOLD
from app.rag.processing.pdf_reader import (
    read_pdf
)

from app.rag.retrieval.embedding_generator import (
    generate_embeddings
)

from app.rag.retrieval.vector_search import (
    semantic_search
)

from app.rag.generation.rag_answer_generator import (
    generate_rag_answer
)

from app.rag.retrieval.reranker import (
    rerank_chunks
)

from app.rag.retrieval.bm25_search import bm25_search

from app.rag.retrieval.hybrid_search import hybrid_search

router = APIRouter()

# Store document chunks
DOCUMENT_CHUNKS = []

# Store embeddings
DOCUMENT_EMBEDDINGS = []

# Store metadata
DOCUMENT_METADATA = []

# Chat memory
CHAT_HISTORY = []


@router.post(
    "/read-pdf"
)
async def read_pdf_file(

    files: List[UploadFile] = File(...),
    policy_type: str = Form(...)
):
    

    global DOCUMENT_CHUNKS
    global DOCUMENT_EMBEDDINGS
    global DOCUMENT_METADATA

    results = []

    for file in files:

        # Save uploaded PDF
        file_path = (
            f"temp_{file.filename}"
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        chunks = read_pdf(
            file_path,
            file.filename,
            policy_type
        )

        if not chunks:

            results.append({

                "filename":
                file.filename,

                "message":
                "Document already exists."
            })

            continue

        # Create metadata
        metadata = []

        for chunk in chunks:

            metadata.append({

                "filename":
                file.filename
            })

        # Store chunks
        DOCUMENT_CHUNKS.extend(
            chunks
        )

        # Store metadata
        DOCUMENT_METADATA.extend(
            metadata
        )


        results.append({

            "filename":
            file.filename,

            "total_chunks":
            len(chunks),

            "message":
            "PDF processed successfully"
        })

    return {

        "uploaded_files":
        results
    }


@router.post(
    "/ask-pdf"
)
async def ask_pdf(

    question,
    policy_type
    
):


    global DOCUMENT_CHUNKS
    global DOCUMENT_EMBEDDINGS
    global DOCUMENT_METADATA
    global CHAT_HISTORY



    # Retrieve relevant chunks
    relevant_chunks = hybrid_search(
        question,
        policy_type=policy_type,
    )

    # Rerank chunks
    relevant_chunks = rerank_chunks(
        question,
        relevant_chunks,
        top_n=3
    )

    if relevant_chunks:

        top_score = relevant_chunks[0]["rerank_score"]

        print(f"Top Rerank Score: {top_score:.4f}")

        if top_score < RERANK_THRESHOLD:

            return {
                "question": question,
                "answer": "I couldn't find this information in the uploaded HR policy documents.",
                "retrieved_chunks": []
            }

    # Merge top chunk contexts
    context = "\n\n".join(

        [
            result["chunk"]

            for result in relevant_chunks
        ]
    )

    if not relevant_chunks:

        return {
            "question": question,
             "answer": "I couldn't find this information in the uploaded HR policy documents.",
            "retrieved_chunks": []
        }

    # Source attribution
    source = (
        relevant_chunks[0]["metadata"]["source"]
    )

    # Build conversation memory
    conversation_context = ""

    for chat in CHAT_HISTORY:

        conversation_context += (

            f"User: {chat['question']}\n"

            f"Assistant: {chat['answer']}\n\n"
        )

    # Combine memory + retrieved context
    full_context = (

        conversation_context

        + "\n\n"

        + context
    )

    # Generate AI answer
    final_answer = (
        generate_rag_answer(

            question,

            full_context
        )
    )

    # Store chat history
    CHAT_HISTORY.append({

        "question":
        question,

        "answer":
        final_answer
    })

    # Keep only recent chats
    if len(CHAT_HISTORY) > 5:

        CHAT_HISTORY.pop(0)

    return {
        "question": question,
        "answer": final_answer,
        "source": source,
        "retrieved_chunks": relevant_chunks,
        "context": full_context
    }


@router.delete("/delete-pdf")
async def delete_pdf(filename: str):

    from app.rag.vectorstore.chroma_client import collection

    collection.delete(
        where={
            "source": filename
        }
    )

    
    return {
        "message": f"{filename} deleted"
    }
