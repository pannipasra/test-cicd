from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing_extensions import Annotated

app = FastAPI()

@app.get("/health")
async def check_health():
    return {"msg": "Hello World"}

@app.get("/ping")
async def ping():
    return "pong"

@app.post("/files/")
async def create_files(
    files: Annotated[List[bytes], File(description="Multiple files as bytes")],
):
    """This function will read files and return size in files array"""
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        List[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    """This function can receive multi-files"""
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)