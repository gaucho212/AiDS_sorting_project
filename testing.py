import time
import random
import sorting  

# Function to generate random lists for benchmarking
def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

# List of sorting algorithms to test
sorting_algorithms = [
    sorting.shell_sort_sedgewick,
    sorting.quick_sort_left_pivot,
    sorting.quick_sort_random_pivot,
    sorting.heap_sort,
    sorting.insertion_sort,
    sorting.selection_sort
]

# List of sizes for the random lists
list_sizes = [100, 1000, 5000, 10000]

# Dictionary to store the results
benchmark_results = {}

# Benchmarking loop
for algorithm in sorting_algorithms:
    algorithm_name = algorithm.__name__
    benchmark_results[algorithm_name] = {}
    for size in list_sizes:
        random_list = generate_random_list(size)
        start_time = time.time()
        algorithm(random_list.copy())  # Use a copy to avoid in-place sorting issues
        end_time = time.time()
        duration = end_time - start_time
        benchmark_results[algorithm_name][size] = duration

# Save the results to a file
with open('benchmark_results.txt', 'w') as file:
    for algorithm_name, results in benchmark_results.items():
        file.write(f"{algorithm_name}:\n")
        for size, duration in results.items():
            file.write(f"  List size {size}: {duration:.6f} seconds\n")
        file.write("\n")