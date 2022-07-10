from os import getcwd
from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "please browse for images at /packages/name_file"}


@app.get("/packages/{name_file}")
async def get_file(name_file: str):
    return FileResponse(path=getcwd() + "/app/packages/" + name_file)
