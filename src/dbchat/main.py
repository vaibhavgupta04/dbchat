from fastapi import FastAPI
from settings.dev_settings import settings
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    print(settings.DATABASE_URL)
    uvicorn.run(app, 
                host="localhost", 
                port=8000)