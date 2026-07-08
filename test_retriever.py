from utils.retriever import retrieve

question = input("Ask a question: ")

results = retrieve(question)

print("\nTop Matches:\n")

for i in range(len(results["documents"][0])):
    print("=" * 60)

    print("File :", results["metadatas"][0][i]["file"])
    print("Page :", results["metadatas"][0][i]["page"])

    print("\nChunk:\n")
    print(results["documents"][0][i])

    print()