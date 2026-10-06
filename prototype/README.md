# Prototype — PoC de STT pt-BR + extração de slots

Objetivo da **Sprint 1–2 (Fundação)**: provar que `voz → dados estruturados` funciona o
suficiente para o MVP, medindo um baseline de qualidade.

O notebook `voice_agent_poc.ipynb` cobre:

1. Transcrição (STT) de áudios de exemplo em pt-BR — Whisper (API ou `faster-whisper`).
2. Extração de intenção + slots a partir do texto (reaproveita o NLU do backend).
3. Esboço de medição de baseline: WER do STT e acurácia de intenção.

## Rodar

```bash
cd prototype
pip install jupyter
# para STT local: pip install faster-whisper
jupyter notebook voice_agent_poc.ipynb
```

> O notebook roda a parte de NLU sem nenhuma chave de API (usa o stub rule_based do backend).
> A parte de STT exige `faster-whisper` (local) ou uma chave da Whisper API.
