"""TTS (text-to-speech) — interface plugável.

Retorno falado do agente. Stub: integrar Azure/Google TTS. Frente Voz/ML implementa.
"""
from __future__ import annotations


def sintetizar(texto: str, lang: str = "pt-BR") -> bytes:
    """Retorna áudio (bytes) do texto. Stub: integrar provedor de TTS na nuvem."""
    raise NotImplementedError("TTS ainda não implementado — ver docs/architecture.md")
