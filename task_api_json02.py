from fastapi import FastAPI
import uvicorn, json, os

app = FastAPI(title="Простой CRUD с JSON")

DATA_FILE = 'users.json'

@app.get("/")
def home():
    """Главная страница"""
    return {"сообщение": "Простой CRUD API", "документация": "/docs"}


def save_users(users):
    """Сохраняет пользователей в JSON файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Возвращает пользователя по ID"""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        users = json.load(f)
    for user in users:
        if user['id'] == user_id:
            return user
    return {"error": "Пользователь не найден"}


@app.on_event("startup")
def startup():
    """Создает тестовых пользователей при первом запуске"""
    if not os.path.exists(DATA_FILE):
        test_users = [
            {"id": 1, "имя": "Иван Петров", "возраст": 25, "email": "ivan@mail.ru"},
            {"id": 2, "имя": "Мария Сидорова", "возраст": 30, "email": "maria@yandex.ru"},
            {"id": 3, "имя": "Петр Иванов", "возраст": 22, "email": "petr@gmail.com"}
        ]
        save_users(test_users)
        print("Созданы тестовые пользователи")


if __name__ == "__main__":
    uvicorn.run("task_api_json:app", host="127.0.0.1", port=8000, reload=True)
