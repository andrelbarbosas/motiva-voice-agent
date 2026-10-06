from app.services import nlu


def test_registrar_extrai_slots_e_pede_confirmacao():
    r = nlu.interpretar("registrar veículo parado no km 123 sentido norte")
    assert r.intencao == "registrar_ocorrencia"
    assert r.slots["tipo"] == "veiculo_parado"
    assert r.slots["km"] == "123"
    assert r.slots["sentido"] == "norte"
    assert r.confirmacao_necessaria is True  # ação crítica


def test_solicitar_apoio_e_critica():
    r = nlu.interpretar("preciso de apoio, mandar guincho")
    assert r.intencao == "solicitar_apoio"
    assert r.confirmacao_necessaria is True


def test_atualizar_status_nao_e_critica():
    r = nlu.interpretar("atualizar status para em atendimento")
    assert r.intencao == "atualizar_status"
    assert r.confirmacao_necessaria is False
