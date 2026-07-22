from pydantic import BaseModel


class ingestion_settings(BaseModel):
    embed_model_ID: str = ""
    gen_model_ID: str = ""

# TODO: think of all settings we might need
# TODO: create settings loading from .env or config stored in a database

