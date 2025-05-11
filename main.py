from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Message(BaseModel):
    message: str

class Conversation(BaseModel):
    messages: List[Message]

conversation_history = []  # To store conversation history

@app.post('/chat')
async def chat(message: Message):
    conversation_history.append(message)  # Add user message to history
    response1 = call_llm(message.message, 'model1')  # Call to LLM model 1
    response2 = call_llm(message.message, 'model2')  # Call to LLM model 2
    conversation_history.append(Message(message=response1))  # Add LLM response to history
    conversation_history.append(Message(message=response2))  # Add LLM response to history
    return {'responses': {'model1': response1, 'model2': response2}, 'conversation': conversation_history}

@app.post('/upload-text/')
async def upload_text(file: UploadFile = File(...)):
    contents = await file.read()
    return {'filename': file.filename, 'content': contents.decode('utf-8')}

@app.post('/upload-image/')
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    return {'filename': file.filename, 'size': len(contents)}

def call_llm(user_input: str, model: str) -> str:
    # Placeholder function to simulate LLM call
    return f'[{model}] You said: {user_input}'

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)