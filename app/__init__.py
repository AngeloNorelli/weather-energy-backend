from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import weather, summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentioals=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

app.include_router(weather.router)
app.include_router(summary.router)