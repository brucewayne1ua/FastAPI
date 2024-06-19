from fastapi import FastAPI
from app.routers import users
from app.database import engine, Base

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключение маршрутов
app.include_router(users.router, prefix="/users")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
