from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from app.core.config import settings
from app.api import auth, users, challenges, admin, scoreboard, submissions
from app.core.security import secure_headers_middleware

app = FastAPI(title="Attack Vector API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(secure_headers_middleware)

@app.get("/api/health")
def health():
    return {"status": "ok"}

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(challenges.router, prefix="/api/challenges", tags=["challenges"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(scoreboard.router, prefix="/api/scoreboard", tags=["scoreboard"])
app.include_router(submissions.router, prefix="/api/submissions", tags=["submissions"])
