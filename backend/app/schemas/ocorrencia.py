"""Schemas Pydantic de entrada/saída da API."""
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class OcorrenciaCreate(BaseModel):
    tipo: str = Field(..., examples=["veiculo_parado"])
    km: str | None = Field(None, examples=["123"])
    sentido: str | None = Field(None, examples=["norte"])
    condicoes: str | None = Field(None, examples=["acostamento, possível necessidade de guincho"])
    criado_por: str = Field(..., examples=["insp.andre"])
    comando: str | None = Field(None, description="Transcrição do que foi dito, para auditoria")
    localizacao: str | None = Field(None, examples=["-23.56,-46.63"])


class OcorrenciaUpdate(BaseModel):
    status: str | None = Field(None, examples=["em_atendimento"])
    condicoes: str | None = None
    usuario: str = Field(..., examples=["insp.andre"])
    comando: str | None = None
    localizacao: str | None = None


class OcorrenciaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tipo: str
    km: str | None
    sentido: str | None
    condicoes: str | None
    status: str
    criado_por: str
    criado_em: datetime
    atualizado_em: datetime


class VozIn(BaseModel):
    """Entrada do endpoint de voz: texto já transcrito (STT acontece no device/serviço)."""

    texto: str = Field(..., examples=["registrar veículo parado no km 123 sentido norte"])
    usuario: str = Field(..., examples=["insp.andre"])
    localizacao: str | None = None


class VozInterpretada(BaseModel):
    """Resultado do NLU: intenção + slots + pedido de confirmação antes de agir."""

    intencao: str
    slots: dict[str, str | None]
    confianca: float
    confirmacao_necessaria: bool
    mensagem_confirmacao: str
