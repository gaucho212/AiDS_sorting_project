import time
import sorting
import sys

sys.setrecursionlimit(10**7)

# Lista algorytmów sortujących
sorting_algorithms = [
    sorting.shell_sort_sedgewick,
    sorting.quick_sort_left_pivot,
    sorting.quick_sort_random_pivot,
    sorting.heap_sort,
    sorting.insertion_sort,
    sorting.selection_sort,
]

# Lista rozmiarów list do testowania
list_sizes = [2**x for x in range(5, 16)]

# Lista kategorii list do testowania
categories = [
    "a_shaped_array",
    "constant_array",
    "decreasing_array",
    "increasing_array",
    "random_array",
]

# Słownik do przechowywania wyników
benchmark_results = {}

# Testowanie algorytmów
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
            )  # Używamy metody copy() aby nie nadpisywać oryginalnej listy
            end_time = time.time()
            print(f"{algorithm_name} {category} {size} {end_time - start_time   }")
            duration = end_time - start_time
            benchmark_results[algorithm_name][category][size] = duration

# Zapisujemy wyniki do pliku
for algorithm_name, category_results in benchmark_results.items():
    for category, results in category_results.items():
        with open(f"{algorithm_name}_{category}.txt", "w") as file:
            for size, duration in results.items():
                file.write(f"{category},{size},{duration:.6f}\n")
            file.write("\n")