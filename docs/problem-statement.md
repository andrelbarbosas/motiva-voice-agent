# Problem Statement

Profissionais de inspeção de tráfego da Motiva atuam na beira da rodovia e hoje precisam
manusear tablet/celular para registrar e consultar ocorrências. Isso **tira a atenção do
ambiente rodoviário (risco de segurança), gera registros incompletos e atrasa a
rastreabilidade**.

Queremos um **agente de voz em pt-BR** que permita registrar, consultar e atualizar
ocorrências por comando falado, com **confirmação explícita antes de ações críticas** e
funcionamento **resiliente a conectividade instável**, mantendo a decisão sempre sob
validação humana.

## Delimitação de escopo

O projeto concentra-se na **interface inteligente de voz** usada pelos profissionais de
campo. O recebimento e processamento centralizado no CCO são tratados em outro projeto
(fora do nosso escopo). Integrações com sistemas legados da Motiva ficam **mockadas** no MVP.
