from fastapi import FastAPI, UploadFile
from methods import hello_ifc
from helpers import file_tools

app = FastAPI()

@app.post("/api/hello-ifc/")
async def create_upload_file(file: UploadFile):
    temp_file_path = file_tools.save_upload_file_tmp(file)
    return await hello_ifc.extract(temp_file_path)