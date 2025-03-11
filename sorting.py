import sys
import random
import time
def quick_sort_random_pivot(data):
    arr = data.copy()
    def partition(low, high):
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[low] = arr[low], arr[pivot_idx]
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(low, high):
        if low < high:
            pivot_idx = partition(low, high)
            quicksort(low, pivot_idx - 1)
            quicksort(pivot_idx + 1, high)
    
    quicksort(0, len(arr) - 1)
    return arr


# Shell Sort z przyrostami Sedgewicka
def shell_sort_sedgewick(data):
    arr = data.copy()
    n = len(arr)
    gaps = []
    i = 0
    while True:
        gap = (4**i + 3 * 2**(i-1) + 1) if i > 0 else 1
        if gap >= n:
            break
        gaps.append(gap)
        i += 1
    gaps = gaps[::-1]
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

# Selection Sort
def selection_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(data):
    arr = data.copy()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# Quick Sort z pivotem skrajnie lewym
def quick_sort_left_pivot(data):
    arr = data.copy()
    def partition(low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(low, high):
        if low < high:
            pivot_idx = partition(low, high)
            quicksort(low, pivot_idx - 1)
            quicksort(pivot_idx + 1, high)
    
    quicksort(0, len(arr) - 1)
    return arr

# Quick Sort z pivotem losowym
def quick_sort_random_pivot(data):
    arr = data.copy()
    def partition(low, high):
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[low] = arr[low], arr[pivot_idx]
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quicksort(low, high):
        if low < high:
            pivot_idx = partition(low, high)
            quicksort(low, pivot_idx - 1)
            quicksort(pivot_idx + 1, high)
    
    quicksort(0, len(arr) - 1)
    return arr

def insertion_sort(data):
    arr = data.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input
    # However, it always uses the sorted function in Python
    start_time=time.time()
    match algorithm:
        case 1: sorted_data= insertion_sort(data)                  # Insertion Sort
        case 2: sorted_data= shell_sort_sedgewick(data)    # Shell Sort
        case 3: sorted_data= selection_sort(data)          # Selection Sort
        case 4: sorted_data= heap_sort(data)               # Heap Sort
        case 5: sorted_data= quick_sort_left_pivot(data)   # Quick Sort (lewy pivot)
        case 6: sorted_data= quick_sort_random_pivot(data) # Quick Sort (losowy pivot)
        case _: 
            print(f"Unknown algorithm: {algorithm}. Using default.")
            sorted_data= sorted(data)
        
    end_time=time.time()
    execution_time=end_time-start_time
    print(f"Czas działania algorytmu: {execution_time:.10f}")
    return sorted_data    
    

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    
    print("Menu Algorytmów sorotwania\n 1.Insertion Sort \n 2.Shell Sort \n 3.Selection Sort \n 4.Heap Sort \n 5.Quick Sort Left Pivot \n 6.Quick Sort Random Pivot\n")
    algorithm_number = int(input("Podaj numer sortowania: "))

    # Read input data from standard input until the end of file (EOF)
    input_data=sys.stdin.read().split()
    try:
        data = [int(x) for x in input_data[:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:])

if __name__ == "__main__":
    main()

#Branch marcin
