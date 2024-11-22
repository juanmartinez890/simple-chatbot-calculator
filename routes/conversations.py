from fastapi import File, UploadFile, APIRouter
from pydantic import UUID4
from schemas.conversation import ConversationMessages
from schemas.message import MessageCreate, MessageResponse
from fastapi import HTTPException
from services.conversation_manager import ConversationManager

router = APIRouter(
    prefix="/api/v1/conversations",
    tags=["Conversations"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Path Not found"}},
)

cm = ConversationManager()
    
# add message to conversation
@router.post("/{conversation_id}/messages")
async def create_new_conversation_message(conversation_id: UUID4, request: MessageCreate) -> MessageResponse:
    return cm.create_conversation_message(
        conversation_id,
        request.request,
    )

#get all conversation messages
@router.get("/")
async def get_all_conversations() -> list[ConversationMessages]:
    all_conversations = cm.get_all_conversations()
    return all_conversations

# get messages in a conversation
@router.get("/{conversation_id}/messages")
async def get_conversation_messages(conversation_id: UUID4) -> ConversationMessages:
    try:
        return cm.get_all_messages_in_conversation(conversation_id)
    except: 
        raise HTTPException(
            status_code=404,
            detail=f"Conversation with ID {conversation_id} does not exist."
        )