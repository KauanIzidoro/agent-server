from fastapi import UploadFile, HTTPException
import shutil 
import os
from settings import SETTINGS

def storage_context_file(user_file: UploadFile):
    """_summary_

    Args:
        user_file (UploadFile): File uploaded by the user.

    Returns:
        HTTP Object: Status of the file upload.

    Description:
        Receive files and storage in local memory.
    """
    try:
        if user_file.filename.endswith((".jpeg",".png",".jpg", ".svg")):
            return "unsupported file format"
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
        
    with open(os.path.join(SETTINGS.USER_FILE_PATH, user_file.filename), "wb") as buffer:
        shutil.copyfileobj(user_file.file, buffer)
    return HTTPException(status_code=201, detail="context file created.")