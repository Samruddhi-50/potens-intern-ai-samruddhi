from utils.pdf_loader import load_documents
from utils.chunker import chunk_documents

# Load all PDF documents
documents = load_documents("documents")

# Split into chunks
chunks = chunk_documents(documents)

print(f"\nTotal Chunks Created: {len(chunks)}\n")

# Display first 5 chunks
for chunk in chunks[:5]:
    print("=" * 60)
    print(f"File : {chunk['file']}")
    print(f"Page : {chunk['page']}")
    print("Chunk Preview:")
    print(chunk["text"][:300])
    print()