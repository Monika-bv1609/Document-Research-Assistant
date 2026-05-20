from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

from app.tools.pdf_reader import (
    read_pdf
)

router = APIRouter()


@router.post(
    "/read-pdf"
)
async def read_pdf_file(

    file: UploadFile = File(...)
):

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

    # Extract text
    pdf_text = read_pdf(
        file_path
    )

    return {
        "pdf_text":
        pdf_text
    }