from utils.retriever import retrieve
from utils.gemini import generate_answer


def detect_contradiction(document1, document2, topic):
    # Retrieve relevant chunks for both documents
    result1 = retrieve(f"{topic} {document1}", top_k=3)
    result2 = retrieve(f"{topic} {document2}", top_k=3)

    chunks1 = result1["documents"][0]
    chunks2 = result2["documents"][0]

    context = "\n\n".join(chunks1) + "\n\n" + "\n\n".join(chunks2)

    prompt = f"""
You are an AI document comparison assistant.

Compare ONLY the provided document excerpts.

Topic: {topic}

Determine whether the documents contradict each other.

Return your answer in this format:

Conflict: Yes or No

Summary:
<Explain your reasoning in a few sentences>

Context:
{context}
"""

    answer = generate_answer(prompt, [])

    # Remove duplicate evidence
    seen = set()
    evidence = []

    for docs, metas in [
        (result1["documents"][0], result1["metadatas"][0]),
        (result2["documents"][0], result2["metadatas"][0]),
    ]:

        for doc, meta in zip(docs, metas):

            key = (meta["file"], meta["page"])

            if key not in seen:
                seen.add(key)

                evidence.append({
                    "file": meta["file"],
                    "page": meta["page"],
                    "snippet": doc[:200] + "..."
                })

    return {
        "answer": answer,
        "evidence": evidence
    }