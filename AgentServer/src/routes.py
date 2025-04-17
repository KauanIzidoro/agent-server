from fastapi import APIRouter, WebSocket, File, UploadFile
from utils import storage_context_file

router = APIRouter()

@router.post('/up-file', tags=['File upload'])
async def upload_file(file: UploadFile = File(...)):
    """_summary_

    Args:
        file (UploadFile, optional): Defaults to File(...).

    Returns:
        file_status (str): Status of the file upload.
    """
    file_status = storage_context_file(user_file=file)
    return file_status

@router.websocket('/chat')
async def rt_chat(ws: WebSocket):
    """_summary_

    Receive messages from user and send to available agents

    Args:
        ws (WebSocket): _description_

    """
    await ws.accept()
    while True:
        user_prompt = await ws.receive_text()
        await ws.send_text(str(user_prompt))

@router.options('/chat-docs', tags=['WebSocket Chat Documentation'])
async def get_websocket_docs():
    """
    Documentation for the WebSocket endpoint
    
    This endpoint provides information about the WebSocket connection at /chat
    
    To connect:
    1. Establish a WebSocket connection to ws://yourdomain/chat
    2. Send text messages to interact with the chat
    3. Receive responses as text
    
    Example client code:
    ```javascript
    const ws = new WebSocket('ws://yourdomain/chat');
    ws.onopen = () => {
        ws.send('Hello from client');
    };
    ws.onmessage = (event) => {
        console.log('Message from server:', event.data);
    };
    ```
    """

