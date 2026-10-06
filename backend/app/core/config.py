"""Configuração central da aplicação (12-factor: tudo via env, com defaults de dev)."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Motiva Voice Agent"
    # SQLite por padrão: roda sem banco externo. Trocar por Postgres em produção.
    database_url: str = "sqlite:///./motiva.db"

    # Provedor de NLU: "rule_based" (stub offline) ou "openai" (function calling).
    nlu_provider: str = "rule_based"
    openai_api_key: str | None = None


settings = Settings()
