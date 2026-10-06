# Motiva Voice Agent 🎙️🛣️

Agente de voz para apoiar profissionais de **inspeção de tráfego** da Motiva em campo:
registrar, consultar e atualizar ocorrências **por comando de voz**, reduzindo digitação e
mantendo a atenção na rodovia — com confirmação antes de ações críticas e rastreabilidade total.

> Desafio de Inovação Aberta · FIAP x Motiva · Turma 2TIAPR · MVP Persona 1 (Agente de Inspeção de Tráfego)

## Visão geral

Fluxo do agente:

```
Áudio (push-to-talk) → STT → NLU (intenção + slots) → Diálogo/Confirmação → Ação → TTS + tela
                                   │
                          camada offline-first (fila outbox + sync) + trilha de auditoria
```

- **Mobile/PWA** (React Native/Expo): captura de voz, GPS, fila offline.
- **Backend** (Python + FastAPI): orquestra STT/NLU/TTS, regras de negócio, auditoria, persistência.
- **Voz híbrida:** STT/TTS na nuvem quando há sinal; fila local + sync quando a conectividade cai.

Documentação detalhada em [`docs/`](docs/).

## Estrutura do repositório

```
motiva-voice-agent/
├── backend/        # FastAPI + serviços de voz/NLU + persistência
├── mobile/         # App/PWA (React Native/Expo) — scaffold
├── prototype/      # Notebook PoC de STT pt-BR + extração de slots
├── docs/           # problem statement, escopo/MVP, user stories, arquitetura, CSD
└── .github/        # CI (lint + testes)
```

## Como rodar o backend

Pré-requisitos: Python 3.11+.

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # ajuste as chaves se for usar STT/LLM na nuvem
uvicorn app.main:app --reload
```

A API sobe em `http://localhost:8000` — docs interativas em `http://localhost:8000/docs`.
Por padrão usa **SQLite** (`motiva.db`), então roda sem precisar de banco externo.

### Com Docker (backend + Postgres)

```bash
docker compose up --build
```

### Testes

```bash
cd backend
pytest
```

## Como contribuir

1. Branch a partir de `main`: `git checkout -b feat/<descricao-curta>`.
2. Commits pequenos e descritivos.
3. Abra um Pull Request — o CI roda lint (`ruff`) e testes (`pytest`).
4. PR precisa de 1 revisão antes do merge. `main` sempre verde.

Convenções e *Definition of Done* em [`docs/`](docs/).

## Time (4 integrantes)

| Frente | Responsabilidade |
|---|---|
| Voz/ML | STT pt-BR, NLU (intenção + slots), notebook PoC |
| Backend | FastAPI, modelo de dados, auditoria, fluxo de confirmação |
| Mobile/Front | App/PWA, push-to-talk, VAD, UI de confirmação e resumo |
| Offline/Infra + Scrum | Fila outbox + sync, Docker/CI, coordenação de sprint |

> Papéis com fronteiras porosas: todos revisam PRs e rodam o app.

## Ética e LGPD

A IA atua como **apoio** — decisões críticas e validações permanecem humanas.
Minimização de dados por perfil, auditoria de acessos e confirmação explícita antes de
registrar, encaminhar ou encerrar. Persona APH (dados sensíveis) fica fora do MVP.

## Licença

Projeto acadêmico FIAP. Uso interno do grupo e da Motiva.
