# Escopo + MVP

## Dentro (Persona 1 — Agente de Inspeção de Tráfego)

Captura push-to-talk → STT → intenção + slots (local, sentido, tipo, condições) →
confirmação falada/visual → registro com auditoria → sync quando houver sinal.
Retorno por voz + tela.

## Fora / mockado

- Processamento no CCO (outro projeto).
- Integrações reais com legado (mockadas o tempo todo).
- Demais personas (Guincho, APH, Supervisor, Coordenador).
- Analytics gerencial.

## Fast-follow opcional (só se sobrar sprint)

US2 consultar procedimento, US4 consultar recursos, US7 resumo do trecho; e 1 US da
Persona 2 (Guincho) reaproveitando o motor de voz.

## Hipótese a validar

> Registrar por voz reduz o tempo de registro e a interação manual em **≥ 50%** frente à
> digitação, com completude de campos obrigatórios **≥ 90%**, sem perda de rastreabilidade.

## Métricas de sucesso

| Métrica | Alvo |
|---|---|
| WER (word error rate) do STT no vocabulário operacional | baixo (medir baseline) |
| Acurácia de intenção (NLU) | ≥ 90% |
| % de campos obrigatórios preenchidos | ≥ 90% |
| Tempo médio de registro por voz vs digitação | −50% |
| % de ocorrências sincronizadas sem perda após queda de sinal | 100% |
| Confirmação antes de ação crítica | 100% |

## Roadmap (6 meses · largada 14/10/2026)

| Mês | Sprints | Datas | Entrega |
|---|---|---|---|
| 1 | 1–2 | 14/10 → 10/11 | Fundação: repo, CI, notebook PoC STT+NLU |
| 2 | 3–4 | 11/11 → 08/12 | Backend do registro (US1) ponta a ponta via API |
| 3 | 5–6 | 09/12 → 05/01 | Mobile + offline (US1) — ⚠️ recesso na Sprint 6 |
| 4 | 7–8 | 06/01 → 02/02 | Ciclo da ocorrência (US3 + US5) |
| 5 | 9–10 | 03/02 → 02/03 | Ações críticas + encerramento (US6 + US8) |
| 6 | 11–12 | 03/03 → 30/03 | Validação de métricas + pitch + demo |

**Marco de corte:** se ao fim do Mês 3 (05/01) o registro por voz offline não estiver de
pé, cortar US6 antes de US8 (encerrar/rastrear > atalho de apoio).
