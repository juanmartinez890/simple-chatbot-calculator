from dotenv import load_dotenv
from fastapi import FastAPI
from routes import conversations

description = """
Simple chatbot calculator is an api design to assists users perform calculations
without the need of a boring calculator UI. 
"""

load_dotenv()

app = FastAPI(
    title="Simple Chatbot Calculator API",
    description=description,
    version="0.0.1",
    # dependencies=[Depends(get_query_token)],
)

app.include_router(conversations.router)
