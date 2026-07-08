from utils.pdf_loader import load_documents

docs = load_documents("documents")

print(f"\nTotal Pages Loaded: {len(docs)}\n")

for doc in docs:
    print("=" * 60)
    print(f"File : {doc['file']}")
    print(f"Page : {doc['page']}")
    print("Text Preview:")
    print(doc["text"][:300])
    print()