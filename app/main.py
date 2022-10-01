from curses.ascii import FS
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"test": 1}
