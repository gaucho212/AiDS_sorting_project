import sorting
import time
import random

def test_insertion_sort():
    test_cases = [
        [random.randint(0, 500000) for _ in range(500000)],
    ]

    for i, test_case in enumerate(test_cases):
        start_time = time.time()
        sorted_list = sorting.insertion_sort(test_case)
        end_time = time.time()
        print(f"Test case {i+1}: {end_time - start_time:.6f} seconds")

test_insertion_sort()