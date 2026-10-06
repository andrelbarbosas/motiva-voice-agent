"""Modelos de dados: Ocorrencia e AuditLog (trilha imutável de rastreabilidade)."""
from datetime import UTC, datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


def _now() -> datetime:
    return datetime.now(UTC)


class Ocorrencia(Base):
    __tablename__ = "ocorrencias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tipo: Mapped[str] = mapped_column(String(80))          # ex.: "veiculo_parado", "acidente"
    km: Mapped[str | None] = mapped_column(String(20), nullable=True)
    sentido: Mapped[str | None] = mapped_column(String(20), nullable=True)  # norte/sul/leste/oeste
    condicoes: Mapped[str | None] = mapped_column(Text, nullable=True)
    # status: aberta | em_atendimento | encerrada
    status: Mapped[str] = mapped_column(String(30), default="aberta")
    criado_por: Mapped[str] = mapped_column(String(120))
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_now)
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=_now, onupdate=_now
    )


class AuditLog(Base):
    """Append-only: nunca atualizar ou apagar linhas. Uma linha por interação relevante."""

    __tablename__ = "audit_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuario: Mapped[str] = mapped_column(String(120))
    acao: Mapped[str] = mapped_column(String(60))  # registrar | atualizar | encerrar | apoio
    ocorrencia_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    comando: Mapped[str | None] = mapped_column(Text, nullable=True)   # transcrição do que foi dito
    resultado: Mapped[str | None] = mapped_column(Text, nullable=True)
    localizacao: Mapped[str | None] = mapped_column(String(120), nullable=True)  # "lat,lon"
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_now)
