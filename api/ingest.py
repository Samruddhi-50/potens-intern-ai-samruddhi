import chromadb

from utils.pdf_loader import load_documents
from utils.chunker import chunk_documents
from utils.embedding import create_embeddings

# Create Chroma client
client = chromadb.PersistentClient(path="chroma_db")

# Create or get collection
collection = client.get_or_create_collection(
    name="documents"
)

# Load PDFs
documents = load_documents("documents")

print(f"Loaded {len(documents)} pages")

# Chunk PDFs
chunks = chunk_documents(documents)

print(f"Created {len(chunks)} chunks")

# Create embeddings
embeddings = create_embeddings(chunks)

print("Embeddings created")

# Store in ChromaDB
for i, chunk in enumerate(chunks):

    collection.add(

        ids=[str(i)],

        embeddings=[embeddings[i].tolist()],

        documents=[chunk["text"]],

        metadatas=[

            {
                "file": chunk["file"],
                "page": chunk["page"]
            }

        ]

    )

print("Documents stored successfully!")