from fastapi import FastAPI
from app.controllers import weather, summary

app = FastAPI()

app.include_router(weather.router)
app.include_router(summary.router)