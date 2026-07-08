from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for doc in documents:
        text_chunks = splitter.split_text(doc["text"])

        for chunk in text_chunks:
            chunks.append({
                "file": doc["file"],
                "page": doc["page"],
                "text": chunk
            })

    return chunks