from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Quant Research Platform")

app.include_router(router)