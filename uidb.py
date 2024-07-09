import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from fastapi import FastAPI

app = FastAPI()

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-2df8d-default-rtdb.firebaseio.com/'
})

@app.get("/execute/{a}/{b}")
async def add(a: int , b: int):
    x = db.reference('/x')
    y = db.reference('/y')
    x.set(a)
    y.set(b)
    ref = db.reference('/Sum')
    ref.set(a + b)
    snap = db.reference("/").get()
    return {"Result": snap.get('Sum')}