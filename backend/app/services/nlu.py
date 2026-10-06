"""NLU: mapeia fala transcrita -> intenção + slots.

Duas implementações atrás da mesma interface:
- rule_based: stub offline (regex) para o MVP arrancar sem chave de API.
- openai: function calling (a frente Voz/ML pluga aqui depois).

Mantém a regra de negócio independente do provedor.
"""
from __future__ import annotations

import re

from app.core.config import settings
from app.schemas.ocorrencia import VozInterpretada

# Intenções do MVP (Persona 1). Mapeadas às user stories.
INTENCOES = {
    "registrar_ocorrencia": "US1",
    "informar_local_condicoes": "US3",
    "atualizar_status": "US5",
    "solicitar_apoio": "US6",
    "encerrar_atendimento": "US8",
}

# Ações críticas exigem confirmação explícita antes de executar (critério de aceite).
ACOES_CRITICAS = {"registrar_ocorrencia", "solicitar_apoio", "encerrar_atendimento"}

_TIPOS = {
    "veículo parado": "veiculo_parado",
    "veiculo parado": "veiculo_parado",
    "acidente": "acidente",
    "animal na pista": "animal_na_pista",
    "objeto na pista": "objeto_na_pista",
}
_SENTIDOS = ["norte", "sul", "leste", "oeste"]


def _extrair_slots(texto: str) -> dict[str, str | None]:
    t = texto.lower()
    tipo = next((v for k, v in _TIPOS.items() if k in t), None)
    km_match = re.search(r"km\s*(\d+)", t)
    sentido = next((s for s in _SENTIDOS if s in t), None)
    return {
        "tipo": tipo,
        "km": km_match.group(1) if km_match else None,
        "sentido": sentido,
    }


def _classificar_intencao(texto: str) -> tuple[str, float]:
    t = texto.lower()
    if any(p in t for p in ["registrar", "registra", "abrir ocorrência", "nova ocorrência"]):
        return "registrar_ocorrencia", 0.9
    if any(p in t for p in ["encerrar", "finalizar", "fechar ocorrência"]):
        return "encerrar_atendimento", 0.9
    if any(p in t for p in ["apoio", "guincho", "reforço", "socorro"]):
        return "solicitar_apoio", 0.85
    if any(p in t for p in ["atualizar", "status", "mudar para", "em atendimento"]):
        return "atualizar_status", 0.8
    if any(p in t for p in ["condições", "condicao", "localização", "sentido", "km"]):
        return "informar_local_condicoes", 0.7
    return "desconhecida", 0.3


def _mensagem_confirmacao(intencao: str, slots: dict[str, str | None]) -> str:
    if intencao == "registrar_ocorrencia":
        partes = [slots.get("tipo") or "ocorrência"]
        if slots.get("km"):
            partes.append(f"no km {slots['km']}")
        if slots.get("sentido"):
            partes.append(f"sentido {slots['sentido']}")
        return f"Confirmar registro de {' '.join(partes)}? Diga 'sim' para gravar."
    if intencao == "solicitar_apoio":
        return "Confirmar solicitação de apoio operacional? Diga 'sim' para acionar."
    if intencao == "encerrar_atendimento":
        return "Confirmar encerramento do atendimento? Diga 'sim' para encerrar."
    return "Entendi. Confirma a ação?"


def interpretar(texto: str) -> VozInterpretada:
    """Interface única de NLU. Hoje usa rule_based; troca por LLM via settings.nlu_provider."""
    if settings.nlu_provider == "openai" and settings.openai_api_key:
        # TODO(Voz/ML): implementar function calling. Fallback para rule_based por ora.
        pass

    intencao, confianca = _classificar_intencao(texto)
    slots = _extrair_slots(texto)
    critica = intencao in ACOES_CRITICAS
    return VozInterpretada(
        intencao=intencao,
        slots=slots,
        confianca=confianca,
        confirmacao_necessaria=critica,
        mensagem_confirmacao=_mensagem_confirmacao(intencao, slots),
    )
