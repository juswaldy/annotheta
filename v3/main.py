from typing import Optional
from fastapi import FastAPI, Request, UploadFile, File, BackgroundTasks
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image, ImageDraw
import os
import uuid

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

################################################################################
# Configs.

UPLOAD_FOLDER = './input/images'

################################################################################
# Helpers.

def generate_mapping(filepath: str):
    """Generate a mapping between the file and a GUID."""
    return True

def get_image_metadata(filepath: str):
    """Read the given image file and get its metadata."""
    img = Image.open(filepath)

################################################################################
# GET

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
    # return {"message": "Hello World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

################################################################################
# POST

@app.post('/upload')
async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)):

    # Save uploaded file.
    with open('{}/{}'.format(UPLOAD_FOLDER, file.filename), 'wb') as f:
        content = await file.read()
        f.write(content)
        f.close()

    # Process file in background.
    background_tasks.add_task(image_get_metadata, filename=file.filename)
    return JSONResponse(content={'message': 'success'})
