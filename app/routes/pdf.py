from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

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

router = APIRouter()

# Store document chunks
DOCUMENT_CHUNKS = []

# Store embeddings
DOCUMENT_EMBEDDINGS = []


@router.post(
    "/read-pdf"
)
async def read_pdf_file(

    file: UploadFile = File(...)
):

    global DOCUMENT_CHUNKS
    global DOCUMENT_EMBEDDINGS

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

    # Extract chunks
    chunks = read_pdf(
        file_path
    )

    # Store chunks
    DOCUMENT_CHUNKS = chunks

    # Generate embeddings
    DOCUMENT_EMBEDDINGS = (
        generate_embeddings(
            chunks
        )
    )

    return {

        "message":
        "PDF processed successfully.",

        "total_chunks":
        len(chunks)
    }


@router.post(
    "/ask-pdf"
)
async def ask_pdf(

    question: str
):

    global DOCUMENT_CHUNKS
    global DOCUMENT_EMBEDDINGS

    # Check if PDF uploaded
    if not DOCUMENT_CHUNKS:

        return {

            "answer":
            "Please upload a PDF first."
        }

    # Retrieve multiple relevant chunks
    relevant_chunks = semantic_search(

        question,
        DOCUMENT_CHUNKS,
        DOCUMENT_EMBEDDINGS
    )

    # Combine chunks into one context
    combined_context = "\n\n".join(
        relevant_chunks
    )

    # Generate final answer
    final_answer = (
        generate_rag_answer(

            question,
            combined_context
        )
    )

    return {

        "question":
        question,

        "answer":
        final_answer
    }