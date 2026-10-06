"""Fixtures de teste: banco SQLite em arquivo temporário e TestClient."""
import os
import tempfile

import pytest

# Usa um SQLite temporário ANTES de importar a app (que lê settings na importação).
_tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
_tmp.close()
os.environ["DATABASE_URL"] = f"sqlite:///{_tmp.name}"

from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)
