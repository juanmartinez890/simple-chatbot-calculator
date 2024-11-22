from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

from schemas.message import MessageResponse

class ConversationResponse(BaseModel):
    conversation_id: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6", description="The unique ID of the conversation")
    created_at: datetime = Field(..., example="2024-11-17T12:00:00Z", description="The timestamp when the conversation was created")

class ConversationMessages(BaseModel):
    conversation_id: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6", description="The unique ID of the conversation")
    created_at: datetime = Field(..., example="2024-11-17T12:00:00Z", description="The timestamp when the conversation was created")
    messages: list[MessageResponse] = Field(..., description="List of messages in the conversation")
