"""STT (speech-to-text) — interface plugável.

No MVP o áudio costuma ser transcrito no device; este módulo define a interface para
quando o backend precisar transcrever (ex.: fallback na nuvem). Frente Voz/ML implementa.
"""
from __future__ import annotations


def transcrever(audio_bytes: bytes, lang: str = "pt-BR") -> str:
    """Retorna o texto transcrito. Stub: integrar Whisper API / faster-whisper.

    TODO(Voz/ML):
      - cloud: Whisper API quando online
      - local: faster-whisper como fallback offline
    """
    raise NotImplementedError("STT ainda não implementado — ver docs/architecture.md")
