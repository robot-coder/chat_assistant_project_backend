from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Message(BaseModel):
    message: str

class Conversation(BaseModel):
    messages: List[Message]

conversation_history = []  # To store conversation history

@app.post('/chat')
async def chat(message: Message):
    conversation_history.append(message)  # Add user message to history
    response = call_llm(message.message)  # Call to LLM function
    conversation_history.append(Message(message=response))  # Add LLM response to history
    return {'response': response, 'conversation': conversation_history}

@app.post('/upload-text/')
async def upload_text(file: UploadFile = File(...)):
    contents = await file.read()
    return {'filename': file.filename, 'content': contents.decode('utf-8')}

@app.post('/upload-image/')
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    return {'filename': file.filename, 'size': len(contents)}

def call_llm(user_input):
    return f'You said: {user_input}'

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)