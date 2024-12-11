from fastapi import FastAPI
from routers import exemplo

# Inicializa o app
app = FastAPI()

# Define uma Router
app.include_router(exemplo.router, prefix="/exemplo", tags=["exemplo"])
