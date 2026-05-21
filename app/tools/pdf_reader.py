from pypdf import PdfReader

import re

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

            page_text = (
                page.extract_text()
            )

            # Remove weird spacing between characters
            page_text = re.sub(

                r'(?<=\w)\s(?=\w)',

                '',

                page_text
            )

            # Normalize spaces
            page_text = " ".join(
                page_text.split()
            )

            text += (
                page_text
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