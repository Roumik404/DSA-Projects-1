def build_index(docs):
    index = {}
    for doc_id, text in enumerate(docs):
        for word in text.lower().split():
            index.setdefault(word, set()).add(doc_id)
    return index

def search(index, docs, query):
    query = query.lower().strip()
    # Phrase search
    if query.startswith('"') and query.endswith('"'):
        phrase = query.strip('"')
        results = [i for i, doc in enumerate(docs) if phrase in doc.lower()]
        return results

    # AND/OR logic
    if " and " in query:
        words = query.split(" and ")
        sets = [index.get(w.strip(), set()) for w in words]
        results = set.intersection(*sets) if sets else set()
    elif " or " in query:
        words = query.split(" or ")
        sets = [index.get(w.strip(), set()) for w in words]
        results = set.union(*sets) if sets else set()
    else:
        words = query.split()
        results = set()
        scores = {}
        for w in words:
            for doc_id in index.get(w, []):
                results.add(doc_id)
                scores[doc_id] = scores.get(doc_id, 0) + 1
        # Sort by relevance score
        results = sorted(results, key=lambda d: scores[d], reverse=True)
        return results
    return list(results)

def main():
    docs = [
        "Python is great for beginners",
        "Data structures and algorithms are key",
        "Python supports dictionaries and sets"
    ]
    index = build_index(docs)

    while True:
        print("\n--- Search Engine Menu ---")
        print("1. Search")
        print("2. Add Document")
        print("3. Exit")
        choice = input("Choose (1-3): ")

        if choice == "1":
            q = input("Enter search query: ")
            res = search(index, docs, q)
            if res:
                print("\nResults:")
                for r in res:
                    print(f"- {docs[r]}")
            else:
                print("No matches found.")

        elif choice == "2":
            new_doc = input("Enter new document text: ")
            docs.append(new_doc)
            index = build_index(docs)
            print("Document added and index rebuilt.")

        elif choice == "3":
            print("Closing search engine. Bye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
