from fastapi import FastAPI
import uvicorn
from routers import notification
from starlette.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Email Notification API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(notification.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)