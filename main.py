from fastapi import FastAPI, Path, UploadFile, File

app = FastAPI()

@app.get("/hello")
def hello():
    return {"Data": "Hey Hello From Here Also"}

@app.get("/todo")
def todo():
    todos = ["Buy groceries", "Clean the house", "Walk the dog"]
    return {"todos": todos}

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    return {
        "file_size": len(await file.read()) // 1024,
        "file_name": file.filename,
        "file_type": file.content_type
    }

@app.get("/execute/{a}/{b}")
def add(a: int , b: int):
    return {"Result": a + b}
