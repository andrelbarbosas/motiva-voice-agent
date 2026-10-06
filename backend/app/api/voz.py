"""Endpoint de voz: recebe texto transcrito e devolve intenção + slots + confirmação.

O cliente mostra/fala a mensagem de confirmação e só então chama /ocorrencias para agir.
Isso implementa o critério de aceite 'confirmação antes de ação crítica'.
"""
from fastapi import APIRouter

from app.schemas.ocorrencia import VozIn, VozInterpretada
from app.services import nlu

router = APIRouter(prefix="/voz", tags=["voz"])


@router.post("/interpretar", response_model=VozInterpretada)
def interpretar(payload: VozIn) -> VozInterpretada:
    return nlu.interpretar(payload.texto)
