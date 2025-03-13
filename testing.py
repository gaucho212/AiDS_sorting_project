import time
import sorting

# List of sorting algorithms to test
sorting_algorithms = [
    sorting.shell_sort_sedgewick,
    #sorting.quick_sort_left_pivot,
    #sorting.quick_sort_random_pivot,
    sorting.heap_sort,
    sorting.insertion_sort,
    sorting.selection_sort,
]

# List of sizes for the lists
list_sizes = [2**x for x in range(5, 16)]

# List of categories for different list shapes
categories = [
    "a_shaped_array",
    "constant_array",
    "decreasing_array",
    "increasing_array",
    "random_array",
]

# Dictionary to store the results
benchmark_results = {}

# Benchmarking loop
for algorithm in sorting_algorithms:
    algorithm_name = algorithm.__name__
    benchmark_results[algorithm_name] = {}
    for category in categories:
        benchmark_results[algorithm_name][category] = {}
        for size in list_sizes:
            f = open(f"benchmark/{category}_{size:08d}.txt", "r")
            testing_list = [int(x) for x in f.read().split()]
            start_time = time.time()
            algorithm(
                testing_list.copy()
            )  # Use a copy to avoid in-place sorting issues
            end_time = time.time()
            duration = end_time - start_time
            benchmark_results[algorithm_name][category][size] = duration

# Save the results to a file
with open(f'benchmark_results.txt', "w") as file:
    for algorithm_name, categories in benchmark_results.items():
        file.write(f"{algorithm_name}:\n")
        for category, results in categories.items():
            file.write(f"  {category}:\n")
            for size, duration in results.items():
                file.write(f"    List size {size}: {duration:.6f} seconds\n")
            file.write("\n")

