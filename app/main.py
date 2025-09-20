"""Точка входа FastAPI-приложения."""

from fastapi import FastAPI

app = FastAPI(title="Минимальное FastAPI-приложение")


@app.get("/")
async def read_root() -> dict[str, str]:
    """Возвращает приветственное сообщение."""
    return {"message": "Привет, FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
