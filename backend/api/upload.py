from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil

from services.pdf_parser import PDFParser
from services.chunk_service import ChunkService
from services.embedding_service import EmbeddingService
from database.chroma_db import ChromaDBService

router = APIRouter(
    prefix="/upload",
    tags=["Upload PDF"]
)

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_FOLDER = BASE_DIR / "uploads"
UPLOAD_FOLDER.mkdir(exist_ok=True)


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    pages = PDFParser.extract_text(str(destination))

    # Create chunks
    chunks = ChunkService.create_chunks(pages)

    # Generate embeddings
    embedding_service = EmbeddingService()
    embeddings = embedding_service.create_embeddings(chunks)

    # ChromaDB
    db = ChromaDBService()

    # Delete old vectors
    db.reset_collection()

    # Store new vectors
    db.store_embeddings(chunks, embeddings)

    return {
        "message": "PDF Indexed Successfully",
        "filename": file.filename,
        "pages": len(pages),
        "chunks": len(chunks),
        "embeddings": len(embeddings)
    }