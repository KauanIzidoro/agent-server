from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.get('/up-file', tags=['File upload'])
async def upload_file():
    """_summary_

    Args:
        file (UploadFile, optional): Defaults to File(...).

    Returns:
        file_status (str): Status of the file upload.
    """
    return {'message': 'real chat bro'}

@router.websocket('/chat')
async def rt_chat(ws: WebSocket):
    """_summary_

    Args:
        ws (WebSocket): _description_

    """
    pass

