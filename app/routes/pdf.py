from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

from app.tools.pdf_reader import (
    read_pdf
)

from app.tools.retriever import (
    retrieve_relevant_chunks
)

router = APIRouter()

# Store document chunks
DOCUMENT_CHUNKS = []


@router.post(
    "/read-pdf"
)
async def read_pdf_file(

    file: UploadFile = File(...)
):

    global DOCUMENT_CHUNKS

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

    # Retrieve relevant chunks
    relevant_chunks = (
        retrieve_relevant_chunks(

            question,
            DOCUMENT_CHUNKS
        )
    )

    # Generate answer
    if relevant_chunks:

        answer = relevant_chunks[0]

    else:

        answer = (
            "No relevant answer found."
        )

    return {

        "question":
        question,

        "answer":
        answer
    }