from pydantic import BaseModel
from typing import List, Optional
import uuid

class RawEmbedding(BaseModel):
    object: str
    index: int
    embedding: List[float]

class RawEmbeddingsResponse(BaseModel):
    embeddings_raw: List[RawEmbedding]

class FormattedEmbedding(BaseModel):
    id: uuid.UUID
    metadata: dict
    values: List[float]

class FormattedEmbeddings(BaseModel):
    embeddings: List[FormattedEmbedding]