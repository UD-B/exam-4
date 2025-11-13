from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def basic():
    return {"msg": "hi from test"}

@app.get("/test/:name")
def checkups(name: str):
    return {"msg": "name"}

@app.post("/caesar")
def caesar(text):
    return 