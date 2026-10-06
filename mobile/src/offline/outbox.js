// Esboço do padrão outbox (fila offline). Implementar na frente Mobile (Mês 3).
// Objetivo: registrar ações localmente e sincronizar com o backend quando houver sinal.

/**
 * @typedef {Object} OutboxItem
 * @property {string} id            uuid local
 * @property {string} tipo          "registrar" | "atualizar" | "encerrar" | "apoio"
 * @property {object} payload       corpo a enviar ao backend
 * @property {"pendente"|"enviado"|"erro"} status
 * @property {number} criadoEm
 */

// TODO(Mobile): persistir com expo-sqlite; aqui fica só o contrato de interface.
export async function enfileirar(/* item: OutboxItem */) {
  throw new Error('não implementado — ver mobile/README.md (padrão outbox)');
}

export async function sincronizarPendentes(/* apiClient */) {
  // 1) ler itens 'pendente'
  // 2) enviar ao backend com backoff
  // 3) marcar 'enviado' em sucesso; manter 'pendente' em falha de rede
  throw new Error('não implementado — ver mobile/README.md (padrão outbox)');
}
