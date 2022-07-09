from os import getcwd
from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/packages/{name_file}")
async def get_file(name_file: str):
    return FileResponse(path=getcwd() + "/" + name_file)
