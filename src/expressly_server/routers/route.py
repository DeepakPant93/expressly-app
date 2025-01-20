from fastapi import APIRouter
from expressly_server.crew import ExpresslyServer
from expressly_server.schemas.schema import ChatInput, ChatOutput
from fastapi import HTTPException


router = APIRouter()


@router.post("/chat")
async def chat(inputs: ChatInput) -> ChatOutput:

    result = None

    try:
        outputs = ExpresslyServer().crew().kickoff(inputs=inputs.model_dump())

        if outputs is None:
            result = "Please check the inputs and try again. If the issue persists, contact support."
        else:
            result = outputs.raw
    except ValueError as ve:
        raise ValueError(f"Value error occurred: {ve}")
    except Exception as e:
        print(f"An Internal server error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error: Please try again later.")

    return ChatOutput(result=result)
