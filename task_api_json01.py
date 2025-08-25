from fastapi import FastAPI
import uvicorn, json

app = FastAPI(title="Простой CRUD с JSON")

DATA_FILE = 'users.json'

@app.get("/")
def home():
    """Главная страница"""
    return {"сообщение": "Простой CRUD API", "документация": "/docs"}



if __name__ == "__main__":
    uvicorn.run("task_api_json:app", host="127.0.0.1", port=8000, reload=True)

