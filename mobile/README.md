# Mobile — Agente de Voz (React Native / Expo)

App de campo do inspetor de tráfego. Foco: **push-to-talk**, captura de áudio + GPS,
e **fila offline** (outbox) que sincroniza com o backend quando há sinal.

> Entra de fato a partir do **Mês 3** do roadmap. Este diretório é o scaffold inicial.

## Setup (quando a frente Mobile começar)

```bash
cd mobile
npm install
npx expo start
```

## Estrutura

```
src/
├── voice/     # gravação de áudio, VAD (voice activity detection), push-to-talk
├── offline/   # fila outbox (SQLite local) + lógica de sync
├── api/       # cliente HTTP do backend (/voz, /ocorrencias)
└── screens/   # telas: registrar, confirmar, resumo/encerrar
```

## Padrão offline-first (outbox)

1. Toda ação do usuário vira um registro local com `status = pendente`.
2. A UI responde na hora, sem esperar a rede.
3. Um *sync worker* tenta enviar os pendentes ao backend quando há conectividade.
4. Em sucesso, marca `enviado`; em falha, mantém `pendente` e tenta de novo (backoff).

Isso atende o critério de aceite **Continuidade**: nada se perde quando o sinal cai.
