from langchain_docling.loader import DoclingLoader
from pathlib import Path
from schemas import Document


def read_file_from_path(file_path: Path) -> Document:
    assert file_path.is_file(), f"path {file_path} must point to a file"
    loader = DoclingLoader(file_path=str(file_path))
    docs = loader.load()
    return Document(
            document_id=file_path.name,
            document_format=file_path.suffix,
            content=docs)

# TODO: chunking to properly fill Chunk objects
# TODO: embeddings for an embedding function
