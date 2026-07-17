import random
import time

def bubble_sort(arr):
    swaps, comps = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, swaps, comps

def selection_sort(arr):
    swaps, comps = 0, 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return arr, swaps, comps

def insertion_sort(arr):
    swaps, comps = 0, 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0:
            comps += 1
            if arr[j] > key:
                arr[j+1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j+1] = key
    return arr, swaps, comps

def run_algorithm(name, func, arr):
    arr_copy = arr.copy()
    start = time.time()
    sorted_arr, swaps, comps = func(arr_copy)
    end = time.time()
    print(f"\n{name}:")
    print(f"Original: {arr}")
    print(f"Sorted:   {sorted_arr}")
    print(f"Swaps: {swaps}, Comparisons: {comps}, Time: {(end-start):.6f}s")

def main():
    size = int(input("Enter array size: "))
    max_val = int(input("Enter max value: "))
    arr = [random.randint(1, max_val) for _ in range(size)]

    print("\nGenerated Array:", arr)

    run_algorithm("Bubble Sort", bubble_sort, arr)
    run_algorithm("Selection Sort", selection_sort, arr)
    run_algorithm("Insertion Sort", insertion_sort, arr)

if __name__ == "__main__":
    main()
