#from fastapi import APIRouter
#from app.model import RequestState
#from agents.ai_agents import get_response_from_ai_agent

#router = APIRouter()

#ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "gpt-4o-mini"]

#@router.post("/chat")
#def chat_endpoint(request: RequestState):
 #   if request.model_name not in ALLOWED_MODEL_NAMES:
  #      return {"error": "Invalid model name. Kindly select a valid AI model"}
    
   # response = get_response_from_ai_agent(
    #    llm_id=request.model_name,
     #   query=request.messages,
      #  allow_search=request.allow_search,
       # system_prompt=request.system_prompt,
        #provider=request.model_provider,
    #)
    #return response

from fastapi import APIRouter
from app.model import RequestState
from agents.ai_agents import get_response_from_ai_agent
from fastapi.responses import JSONResponse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "gpt-4o-mini"]

@router.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        # Validate model
        if request.model_name not in ALLOWED_MODEL_NAMES:
            return JSONResponse(
                status_code=400,
                content={"response": "❌ Invalid model name. Please select a valid AI model."}
            )

        # Get AI response
        ai_response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider,
        )

        # Log the AI response to inspect its structure
        logging.info(f"AI Response: {ai_response}")

        # Ensure it's a valid response (dict with 'response' key)
        if isinstance(ai_response, dict):
            # Check if 'response' key exists in the AI response
            if "response" in ai_response:
                return JSONResponse(content=ai_response)
            # Log the structure of ai_response if 'response' is missing
            else:
                logging.error(f"Unexpected AI response format: Missing 'response' key. Response: {ai_response}")
                return JSONResponse(
                    status_code=500,
                    content={"response": "⚠️ Unexpected response format from AI agent. Missing 'response' key."}
                )
        else:
            # Log when AI response is not a dictionary
            logging.error(f"Unexpected AI response format: Expected dictionary, but got {type(ai_response)}. Response: {ai_response}")
            return JSONResponse(
                status_code=500,
                content={"response": "⚠️ Unexpected response format from AI agent. Expected dictionary."}
            )

    except Exception as e:
        # Catch any other unexpected errors
        logging.exception("Internal server error")
        return JSONResponse(
            status_code=500,
            content={"response": f"💥 Internal server error: {str(e)}"}
        )
