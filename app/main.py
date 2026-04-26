from fastapi import FastAPI

from app.api.user_router import router as user_router

app = FastAPI(
    title="Banking Clean API",
    description="Backend financiero con Clean Architecture",
    version="1.0.0"
)

app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)