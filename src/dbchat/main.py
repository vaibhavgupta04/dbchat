from typing import Union
from fastapi import FastAPI
from src.models.openai import query
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    print(query)
    uvicorn.run(app, 
                host="localhost", 
                port=8000)