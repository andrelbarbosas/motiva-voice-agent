# Arquitetura + Stack

## Fluxo do agente

```
┌─────────────┐   áudio    ┌──────┐  texto  ┌──────┐ intenção+slots ┌───────────────┐
│ Mobile/PWA  │ ─────────▶ │ STT  │ ──────▶ │ NLU  │ ─────────────▶ │ Orquestrador  │
│ push-to-talk│            └──────┘         └──────┘                │ + Confirmação │
│  VAD · GPS  │ ◀───────── voz/TTS + tela ◀──────────────────────── │  (guardrails) │
└─────────────┘                                                      └──────┬────────┘
       │ offline-first (fila outbox + sync)                                 │ ações
       ▼                                                                     ▼
  SQLite local  ◀───────────────── sync quando há sinal ─────────▶  API (FastAPI)
                                                                     ├─ Ocorrências (CRUD)
                                                                     └─ Auditoria (imutável)
                                                                            │
                                                                     PostgreSQL
```

## Stack

| Camada | Escolha | Por quê |
|---|---|---|
| Mobile/PWA | React Native (Expo) | microfone, GPS, storage local; roda no tablet do inspetor |
| Fila offline | SQLite local (padrão outbox) | resiliência à conectividade instável (critério *Continuidade*) |
| Backend | Python + FastAPI (async, WebSocket, Pydantic) | aderente ao time Python/ML; schemas fortes |
| STT pt-BR | híbrido: cloud (Whisper API/Google/Azure) + fallback local (faster-whisper) | funciona com e sem sinal |
| NLU | LLM com *function calling* (fala → intenção + slots) | evita treinar classificador do zero no MVP |
| TTS | cloud (Azure/Google) | resposta falada natural |
| DB | PostgreSQL (ocorrências + auditoria imutável) | rastreabilidade |
| Infra/Eng | Docker Compose, GitHub (main/feature), GitHub Actions (lint + testes) | reprodutível em qualquer máquina |

## Princípios de design

- **Confirmação antes de ação crítica** é regra do orquestrador, não opção de UI.
- **Auditoria imutável:** todo registro guarda quem/quando/onde/comando/resultado.
- **IA como apoio:** decisões críticas e validações permanecem humanas.
- **Interfaces plugáveis** para STT/NLU/TTS: trocar provedor sem mexer na regra de negócio.

## LGPD / ética

Minimização de dados por perfil; APH fora do MVP; auditoria de acessos; confirmação explícita.
