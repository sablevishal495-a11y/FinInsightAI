from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.query import router as query_router
from api.upload import router as upload_router

app = FastAPI(
    title="FinInsight API",
    description="Enterprise Financial Document Intelligence",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(query_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to FinInsight 🚀",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }