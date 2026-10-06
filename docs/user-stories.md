# User Stories — MVP (Persona 1: Agente de Inspeção de Tráfego)

Formato: *Como [persona], quero [ação], para [benefício].*

## US1 — Registrar ocorrência
Como agente de inspeção de tráfego, quero registrar uma ocorrência por comando de voz,
para reduzir a digitação e manter minha atenção na via.
**Aceite:** extrai tipo/local/sentido; **repete os dados e pede confirmação explícita**
antes de gravar; persiste usuário, data, hora, GPS, comando e resultado.

## US3 — Informar localização e condições
Como agente de inspeção, quero informar verbalmente localização, sentido da via e
condições, para gerar um registro estruturado e preciso.
**Aceite:** campos livres viram estrutura (km/sentido/condição); em ambiguidade, o agente
pergunta em vez de assumir.

## US5 — Atualizar status
Como agente de inspeção, quero atualizar por voz o status da ocorrência, para manter os
sistemas com informação recente.
**Aceite:** atualização vinculada a uma ocorrência existente; confirmação antes de aplicar;
funciona offline com fila.

## US6 — Solicitar apoio
Como agente de inspeção, quero solicitar apoio operacional por voz, para agilizar o
acionamento sem manusear o dispositivo.
**Aceite:** ação crítica → confirmação obrigatória; registra o pedido; se sem sinal,
enfileira e avisa o usuário.

## US8 — Encerrar atendimento
Como agente de inspeção, quero encerrar por voz descrevendo as providências, para garantir
rastreabilidade e completude.
**Aceite:** gera **resumo estruturado e editável** antes do envio final; bloqueia
encerramento com campos obrigatórios faltando.

---

## Critérios transversais de aceite (todas as US)

1. **Compreensão** — reconhecer o vocabulário operacional; pedir esclarecimento em ambiguidade.
2. **Confirmação** — repetir dados críticos e confirmar antes de registrar/encaminhar/encerrar.
3. **Rastreabilidade** — registrar usuário, data, hora, localização, comando, resposta e resultado.
4. **Segurança** — mínima interação manual; não induzir perda de atenção na via.
5. **Continuidade** — informar indisponibilidade e preservar dados para sincronização.
6. **Privacidade** — expor o mínimo de dados pessoais/sensíveis por perfil.
7. **Governança** — respeitar permissões por persona; decisão crítica sob validação humana.
8. **Qualidade** — resumo estruturado e editável antes do envio definitivo.

## Fast-follow (fora do MVP inicial)

US2 Consultar procedimento · US4 Consultar recursos acionados · US7 Ouvir resumo do trecho.
