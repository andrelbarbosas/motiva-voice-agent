"""CRUD de ocorrências (US1, US3, US5, US8). Toda ação grava auditoria."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.ocorrencia import Ocorrencia
from app.schemas.ocorrencia import OcorrenciaCreate, OcorrenciaOut, OcorrenciaUpdate
from app.services import ocorrencia as svc

router = APIRouter(prefix="/ocorrencias", tags=["ocorrencias"])


def _get_or_404(db: Session, ocorrencia_id: int) -> Ocorrencia:
    oc = db.get(Ocorrencia, ocorrencia_id)
    if oc is None:
        raise HTTPException(status_code=404, detail="Ocorrência não encontrada")
    return oc


@router.post("", response_model=OcorrenciaOut, status_code=201)
def criar(dados: OcorrenciaCreate, db: Session = Depends(get_db)) -> Ocorrencia:
    """US1 — registrar ocorrência (o cliente já confirmou com o usuário via /voz)."""
    return svc.criar(db, dados)


@router.get("", response_model=list[OcorrenciaOut])
def listar(db: Session = Depends(get_db)) -> list[Ocorrencia]:
    return db.query(Ocorrencia).order_by(Ocorrencia.criado_em.desc()).all()


@router.get("/{ocorrencia_id}", response_model=OcorrenciaOut)
def obter(ocorrencia_id: int, db: Session = Depends(get_db)) -> Ocorrencia:
    return _get_or_404(db, ocorrencia_id)


@router.patch("/{ocorrencia_id}", response_model=OcorrenciaOut)
def atualizar(
    ocorrencia_id: int, dados: OcorrenciaUpdate, db: Session = Depends(get_db)
) -> Ocorrencia:
    """US3/US5 — atualizar condições/status."""
    oc = _get_or_404(db, ocorrencia_id)
    return svc.atualizar(db, oc, dados)


@router.post("/{ocorrencia_id}/encerrar", response_model=OcorrenciaOut)
def encerrar(
    ocorrencia_id: int, usuario: str, comando: str | None = None, db: Session = Depends(get_db)
) -> Ocorrencia:
    """US8 — encerrar; bloqueia se faltar campo obrigatório."""
    oc = _get_or_404(db, ocorrencia_id)
    try:
        return svc.encerrar(db, oc, usuario=usuario, comando=comando)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e
