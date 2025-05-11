from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post('/chat')
async def chat(message: Message):
    # Here you would integrate with LiteLLM or any other LLM
    response = f'You said: {message.message}'  # Placeholder response
    return {'response': response}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)