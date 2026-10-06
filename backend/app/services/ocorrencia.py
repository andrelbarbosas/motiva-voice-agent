"""Regras de negócio de ocorrências, sempre gravando trilha de auditoria."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.ocorrencia import AuditLog, Ocorrencia
from app.schemas.ocorrencia import OcorrenciaCreate, OcorrenciaUpdate

CAMPOS_OBRIGATORIOS_ENCERRAMENTO = ("condicoes",)


def _audit(
    db: Session,
    *,
    usuario: str,
    acao: str,
    ocorrencia_id: int | None = None,
    comando: str | None = None,
    resultado: str | None = None,
    localizacao: str | None = None,
) -> None:
    db.add(
        AuditLog(
            usuario=usuario,
            acao=acao,
            ocorrencia_id=ocorrencia_id,
            comando=comando,
            resultado=resultado,
            localizacao=localizacao,
        )
    )


def criar(db: Session, dados: OcorrenciaCreate) -> Ocorrencia:
    oc = Ocorrencia(
        tipo=dados.tipo,
        km=dados.km,
        sentido=dados.sentido,
        condicoes=dados.condicoes,
        criado_por=dados.criado_por,
    )
    db.add(oc)
    db.flush()  # garante oc.id antes do audit
    _audit(
        db,
        usuario=dados.criado_por,
        acao="registrar",
        ocorrencia_id=oc.id,
        comando=dados.comando,
        resultado=f"ocorrencia {oc.id} criada",
        localizacao=dados.localizacao,
    )
    db.commit()
    db.refresh(oc)
    return oc


def atualizar(db: Session, oc: Ocorrencia, dados: OcorrenciaUpdate) -> Ocorrencia:
    if dados.status is not None:
        oc.status = dados.status
    if dados.condicoes is not None:
        oc.condicoes = dados.condicoes
    _audit(
        db,
        usuario=dados.usuario,
        acao="atualizar",
        ocorrencia_id=oc.id,
        comando=dados.comando,
        resultado=f"status={oc.status}",
        localizacao=dados.localizacao,
    )
    db.commit()
    db.refresh(oc)
    return oc


def campos_pendentes_para_encerrar(oc: Ocorrencia) -> list[str]:
    """US8: não deixar encerrar com campos obrigatórios faltando."""
    return [c for c in CAMPOS_OBRIGATORIOS_ENCERRAMENTO if not getattr(oc, c)]


def encerrar(db: Session, oc: Ocorrencia, usuario: str, comando: str | None = None) -> Ocorrencia:
    pendentes = campos_pendentes_para_encerrar(oc)
    if pendentes:
        raise ValueError(f"Campos obrigatórios faltando: {', '.join(pendentes)}")
    oc.status = "encerrada"
    _audit(
        db,
        usuario=usuario,
        acao="encerrar",
        ocorrencia_id=oc.id,
        comando=comando,
        resultado="ocorrencia encerrada",
    )
    db.commit()
    db.refresh(oc)
    return oc
