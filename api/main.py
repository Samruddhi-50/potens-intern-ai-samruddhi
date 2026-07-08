from fastapi import FastAPI
from pydantic import BaseModel

from utils.retriever import retrieve
from utils.gemini import generate_answer
from utils.contradiction import detect_contradiction

app = FastAPI(
    title="Potens AI/ML RAG API",
    version="1.0.0"
)

class AskRequest(BaseModel):
    question: str


class ContradictRequest(BaseModel):
    document1: str
    document2: str
    topic: str


@app.get("/")
def home():
    return {
        "message": "Potens AI/ML Assignment API is running!"
    }


@app.post("/ask")
def ask(request: AskRequest):

    # Retrieve relevant chunks
    results = retrieve(request.question)

    chunks = results["documents"][0]

    # Generate answer
    answer = generate_answer(request.question, chunks)

    citations = []

    # Remove duplicate citations
    seen = set()
    citations = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        
        key = (meta["file"], meta["page"])
        
        if key not in seen:
            seen.add(key)
            
            citations.append(
                {
                    "file": meta["file"],
                    "page": meta["page"],
                    "snippet": doc[:200] + "..."
               }
           )

    return {
        "answer": answer,
        "citations": citations
    }


@app.post("/contradict")
def contradict(request: ContradictRequest):

    result = detect_contradiction(
        request.document1,
        request.document2,
        request.topic
    )

    return result    