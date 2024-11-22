from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class MessageCreate(BaseModel):
    request: str = Field(..., example="How much is 2+2?", description="The request message from the guest")

    class Config:
        schema_extra = {
            "example": {
                "request": "How much is 2+2?"
            }
        }

class MessageResponse(BaseModel):
    message_id: UUID = Field(..., example="2d85f64-5717-4562-b3fc-2c963f66afa6", description="The unique ID of the message")
    request: str
    response: str = Field(..., example="2+2 is 4", description="The response message from the agent or system")
    created_at: datetime = Field(..., example="2024-11-17T12:05:00Z", description="The timestamp when the message was created")