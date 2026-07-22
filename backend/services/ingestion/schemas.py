from typing import List, Any
from pydantic import BaseModel
from langchain_core.documents.base import Document as langchain_doc


class Chunk(BaseModel):
    document_id: str = ""
    chunk_id: str = ""
    section_id: str = ""
    content: str = ""
    searchable_text: str = ""
    embedding: Any # TODO: define what this type will be


class Document(BaseModel):
    document_id: str = ""
    document_format: str = ""
    content: List[langchain_doc] | langchain_doc
