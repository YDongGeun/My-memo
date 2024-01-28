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

@app.put('/memoes/{memo_id}')
def put_memo(req_memo:Memo):
    for memo in memoes:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return '성공했습니다.'
    return 'not memo'

@app.delete("/memoes/{memo_id}")
def delete_memo(memo_id:int):
    for index, memo in enumerate(memoes):
        if memo.id == memo_id:
            memoes.pop(index)
            return '성공했습니다.'
    return 'not memo', print(memoes)

app.mount("/memo", StaticFiles(directory="static", html=True), name="static")