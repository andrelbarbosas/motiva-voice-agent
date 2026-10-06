# Contribuindo

## Fluxo de branches
- `main` é sempre estável e verde (CI passando).
- Trabalho em branches `feat/<descricao>`, `fix/<descricao>` ou `docs/<descricao>`.
- Pull Request com pelo menos **1 revisão** antes do merge.

## Commits
- Mensagens curtas e no imperativo: "adiciona fluxo de confirmação do registro".
- Commits pequenos e coesos (um propósito por commit).

## Definition of Done (DoD)
Uma user story está "pronta" quando:
1. Código implementado e revisado em PR.
2. Testes cobrindo o caminho feliz + ao menos um caso de borda.
3. CI verde (ruff + pytest).
4. Critérios de aceite da US atendidos (ver `docs/user-stories.md`).
5. Doc atualizada se mudou comportamento ou setup.

## Cerimônias (Scrum, sprints de 2 semanas)
- **Daily** assíncrona (ou rápida): o que fiz / farei / impedimentos.
- **Planning** no início da sprint: puxar do backlog priorizado.
- **Review + Retro** no fim: demo do incremento e ajustes de processo.

## Ambiente
- Backend: Python 3.11+, `pip install -r backend/requirements.txt`.
- Rodar local sem banco externo (SQLite default); Postgres via `docker compose up`.
