import os

from dotenv import load_dotenv

load_dotenv()

RERANK_THRESHOLD = float(
    os.getenv(
        "RERANK_THRESHOLD",
        "0.30"
    )
)