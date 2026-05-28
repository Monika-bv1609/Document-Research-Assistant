from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.routes.pdf import (
    router as pdf_router
)

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    # allow_origins=["*"],
    allow_origins=[

        "http://localhost:5173",

        "https://ai-research-assistant-navy.vercel.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(
    pdf_router
)