from fastapi import FastAPI
import uvicorn, json, os

app = FastAPI(title="Простой CRUD с JSON")

DATA_FILE = 'users.json'

def load_users():
    return json.load(open(DATA_FILE, 'r', encoding='utf-8'))

@app.get("/")
def home():
    """Главная страница"""
    return {"сообщение": "Простой CRUD API", "документация": "/docs"}

@app.get("/users")
def get_users():
    """Возвращает список пользователей"""   
    return load_users()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Возвращает пользователя по ID"""  
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            return user
    return {"error": "Пользователь не найден"}

@app.post("/users")
def create_user(user: dict):
    """Создает нового пользователя"""
    users = load_users()
    # Проверяем, что email уникальный
    for u in users:
        if u['email'] == user['email']:
            return {"error": "Пользователь с таким email уже существует"}
    user['id'] = len(users) + 1
    users.append(user)
    save_users(users)
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    """Обновляет пользователя по ID"""
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            user.update(updated_user)
            save_users(users)
            return user
    return {"error": "Пользователь не найден"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Удаляет пользователя по ID"""
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            save_users(users)
            return {"message": "Пользователь удален"}
    return {"error": "Пользователь не найден"}


# поиск юзера по имени
@app.get("/users/search/{name}")
def search_user(name: str):
    """Поиск пользователя по имени"""
    users = load_users()
    print(1, name)
    for user in users:
        if name.lower() in user['имя'].lower():
            return user
    return {"error": "Пользователь не найден"}



def save_users(users):
    """Сохраняет пользователей в JSON файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

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