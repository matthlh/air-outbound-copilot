from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    llm_provider: str = os.getenv("LLM_PROVIDER", "anthropic")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./data/results.db")
    n8n_webhook_url: str = os.getenv("N8N_WEBHOOK_URL", "")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
