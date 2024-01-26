from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel): 
    id:int
    content:str
    
memoes = []

app = FastAPI()

@app.post('/memoes')
def create_memo(memo:Memo):
    memoes.append(memo)
    return 'memo creat complete!'

@app.get('/memoes')
def read_memo():
    return memoes

app.mount("/memo", StaticFiles(directory="static", html=True), name="static")