"""Fluxo ponta a ponta de US1 → US3/US5 → US8, incluindo bloqueio de encerramento."""


def test_fluxo_registrar_atualizar_encerrar(client):
    # US1 — registrar
    r = client.post(
        "/ocorrencias",
        json={
            "tipo": "veiculo_parado",
            "km": "123",
            "sentido": "norte",
            "criado_por": "insp.andre",
            "comando": "registrar veículo parado no km 123 sentido norte",
        },
    )
    assert r.status_code == 201
    oc = r.json()
    oc_id = oc["id"]
    assert oc["status"] == "aberta"

    # US8 — encerrar sem condições deve FALHAR (campo obrigatório faltando)
    r = client.post(f"/ocorrencias/{oc_id}/encerrar", params={"usuario": "insp.andre"})
    assert r.status_code == 422

    # US3/US5 — informar condições e atualizar status
    r = client.patch(
        f"/ocorrencias/{oc_id}",
        json={
            "status": "em_atendimento",
            "condicoes": "acostamento, sem vítimas",
            "usuario": "insp.andre",
        },
    )
    assert r.status_code == 200
    assert r.json()["status"] == "em_atendimento"

    # US8 — agora encerra com sucesso
    r = client.post(f"/ocorrencias/{oc_id}/encerrar", params={"usuario": "insp.andre"})
    assert r.status_code == 200
    assert r.json()["status"] == "encerrada"


def test_obter_inexistente_404(client):
    assert client.get("/ocorrencias/999999").status_code == 404
