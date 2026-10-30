import timeit
import random
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def get_random_list(n):
    return [random.randint(0, 10000) for _ in range(n)]

def run_benchmarks():
    random.seed(42)
    results = [] 

    print("Запуск бенчмарков (пожалуйста, подождите)...")

    # 1. Бенчмарк сортировок
    for n in (1000, 10000, 100000):
        data = get_random_list(n)
        
        # Замер встроенного sorted
        t_sorted = timeit.timeit(lambda: sorted(data), number=1)
        results.append(("sort", n, "sorted", round(t_sorted, 5)))
        
        # Замеры наших сортировок
        for fn in (bubble_sort, insertion_sort, selection_sort):
            if n == 100000:
                # ПРОПУСКАЕМ долгие сортировки на 100к
                results.append(("sort", n, fn.__name__, ">60"))
                print(f"  {fn.__name__} на n={n}: пропущено (заняло бы > 60 сек)")
            else:
                t = timeit.timeit(lambda: fn(data), number=1)
                results.append(("sort", n, fn.__name__, round(t, 5)))
                print(f"  {fn.__name__} на n={n}: {t:.4f} сек")

    # 2. Бенчмарк поиска
    n_search = 100000
    search_data = get_random_list(n_search)
    sorted_search_data = sorted(search_data)
    targets = [random.choice(search_data) for _ in range(10000)]
    
    t_linear = timeit.timeit(lambda: [linear_search(search_data, t) for t in targets], number=1)
    results.append(("search", n_search, "linear_search", round(t_linear, 5)))
    
    t_bin_sort = timeit.timeit(lambda: sorted(search_data), number=1)
    t_bin_search = timeit.timeit(lambda: [binary_search(sorted_search_data, t) for t in targets], number=1)
    results.append(("search", n_search, "binary_search (with sort)", round(t_bin_sort + t_bin_search, 5)))
    results.append(("search", n_search, "binary_search (only)", round(t_bin_search, 5)))

    # 3. Бенчмарк Two Sum
    for n in (1000, 10000):
        data = get_random_list(n)
        target = data[0] + data[1] # Гарантируем, что пара есть
        
        t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
        
        results.append(("two_sum", n, "two_sum_brute", round(t_brute, 5)))
        results.append(("two_sum", n, "two_sum_fast", round(t_fast, 5)))
        
    return results

def print_table(results):
    print("\n" + "="*60)
    print(f"{'Task':<10} | {'n':<8} | {'Impl':<25} | {'Seconds':<10}")
    print("-" * 60)
    for row in results:
        print(f"{row[0]:<10} | {row[1]:<8} | {row[2]:<25} | {row[3]:<10}")
    print("="*60 + "\n")

if __name__ == "__main__":
    data = run_benchmarks()
    print_table(data)
    
    csv_path = "data/lab07/bench.csv"
    write_csv(data, csv_path, header=("task", "n", "impl", "seconds"))
    print(f"Данные сохранены в {csv_path}")