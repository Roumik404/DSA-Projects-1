from collections import OrderedDict

cache = OrderedDict()
capacity = 5
hits = 0
misses = 0

def access(key, value=None):
    global hits, misses
    if key in cache:
        hits += 1
        cache.move_to_end(key)
        print(f"Cache hit: {key} -> {cache[key]}")
    else:
        misses += 1
        print(f"Cache miss: {key}")
        if value is not None:
            if len(cache) >= capacity:
                oldest = next(iter(cache))
                print(f"Evicting (LRU): {oldest}")
                del cache[oldest]
            cache[key] = value
            print(f"Inserted: {key} -> {value}")

def show_cache():
    print("\n--- Cache State ---")
    for k, v in cache.items():
        print(f"{k}: {v}")
    print(f"Hits: {hits} | Misses: {misses} | Hit Ratio: {(hits/(hits+misses)):.2f}" if (hits+misses) else "No accesses yet.")

def main():
    while True:
        print("\n--- Cache Menu ---")
        print("1. Access Key")
        print("2. Show Cache")
        print("3. Exit")
        choice = input("Choose (1-3): ")

        if choice == "1":
            k = input("Enter key: ")
            v = input("Enter value (or blank if just read): ")
            access(k, v if v else None)
        elif choice == "2":
            show_cache()
        elif choice == "3":
            print("Closing Cache Simulator. Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
