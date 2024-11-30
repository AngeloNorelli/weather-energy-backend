from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import weather, summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(weather.router)
app.include_router(summary.router)