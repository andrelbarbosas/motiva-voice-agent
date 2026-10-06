"""Ponto de entrada da API do agente de voz Motiva."""
from fastapi import FastAPI

from app.api import ocorrencias, voz
from app.core.config import settings
from app.db.session import Base, engine

# No MVP criamos as tabelas direto. Em produção, migrar para Alembic.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="MVP Persona 1 — Agente de Inspeção de Tráfego (FIAP x Motiva)",
    version="0.1.0",
)

app.include_router(voz.router)
app.include_router(ocorrencias.router)


@app.get("/health", tags=["infra"])
def health() -> dict[str, str]:
    return {"status": "ok", "app": settings.app_name}
