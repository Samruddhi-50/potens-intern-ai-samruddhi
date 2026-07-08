from utils.retriever import retrieve
from utils.gemini import generate_answer

question = input("Ask a question: ")

results = retrieve(question)

chunks = results["documents"][0]

answer = generate_answer(question, chunks)

print("\n" + "=" * 70)
print("ANSWER")
print("=" * 70)

print(answer)

print("\n" + "=" * 70)
print("CITATIONS")
print("=" * 70)

for meta in results["metadatas"][0]:
    print(f"{meta['file']} | Page {meta['page']}")
    