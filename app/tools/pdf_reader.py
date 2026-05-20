from pypdf import PdfReader

from app.tools.text_chunker import (
    chunk_text
)


def read_pdf(
    file_path: str
):

    try:

        # Open PDF
        reader = PdfReader(
            file_path
        )

        text = ""

        # Read all pages
        for page in reader.pages:

            text += (
                page.extract_text()
                + "\n"
            )

        # Create chunks
        chunks = chunk_text(
            text
        )

        return chunks

    except Exception as e:

        print(e)

        return (
            "PDF reading failed."
        )