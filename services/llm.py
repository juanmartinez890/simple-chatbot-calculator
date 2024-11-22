import os
import openai
from fastapi import HTTPException
from schemas.llm import MessageList

class LLMService:

    def __init__(self):
        self.api_key = os.getenv("OPEN_AI_API_KEY")
        self.model = os.getenv("OPEN_AI_COMPLETITION_MODEL_NAME")

    def compose_response(
            self,
            messages: MessageList,
            enable_function_calls: bool
        ) -> dict:
        try:
            
            openai.api_key = self.api_key

            tool_choice = "none"

            if enable_function_calls:
                tool_choice = "required"

            completition_response = openai.ChatCompletion.create(
            model= self.model,
            temperature= 0, # to environment variable
            messages=messages,
            tools = self.get_function_calls(),
            tool_choice=tool_choice
            )
            
            if(len(completition_response.choices)> 0):
                if(completition_response.choices[0].message.content):
                    return completition_response.choices[0].message.content
                elif (completition_response.choices[0].message.tool_calls):   
                    tool_calls = completition_response.choices[0].message.tool_calls
                    if(len(tool_calls)> 0):
                        return tool_calls[0].function.arguments

            return "sorry, I could not find the information you requested."
        
        except openai.error.APIError as e:
            raise HTTPException(
                status_code=404,
                detail=f"OpenAI API returned an API Error: {e}"
            )
        
        except openai.error.APIConnectionError as e:
            raise HTTPException(
                status_code=404,
                detail=f"Failed to connect to OpenAI API: {e}"
            )
        
        except openai.error.RateLimitError as e:
            raise HTTPException(
                status_code=404,
                detail=f"OpenAI API request exceeded rate limit: {e}"
            )
        
        except openai.error.AuthenticationError as e:
            raise HTTPException(
                status_code=404,
                detail=f"OpenAI API authentication error: {e}"
            )
        
    def get_function_calls(self) -> list[dict]:
        return [
            {
            "type": "function",
                "function": {
                    "name": "perform_simple_calculation",
                    "description": "This function should extract values, operator, and result of calculation.",
                    "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {
                        "type": "string",
                        "description": "operation elements and operator. "
                        },
                        "result": {
                        "type": "integer",
                        "description": "result of the operation"
                        }
                    },
                    "required": ["operation", "result"]
                    }
                }
            }
        ]
