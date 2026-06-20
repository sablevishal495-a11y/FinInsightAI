from fastapi import APIRouter
from pydantic import BaseModel

from services.embedding_service import EmbeddingService
from database.chroma_db import ChromaDBService
from services.groq_service import GroqService

router = APIRouter(
    prefix="/query",
    tags=["Ask PDF"]
)


class QueryRequest(BaseModel):
    question: str


@router.post("/")
async def ask_question(request: QueryRequest):

    # Create fresh instances for every request
    embedding_service = EmbeddingService()
    db = ChromaDBService()

    question_embedding = embedding_service.model.encode(
        request.question,
        convert_to_numpy=True
    )

    results = db.search(question_embedding)

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

    answer = GroqService.generate_answer(
        request.question,
        documents
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": metadata
    }