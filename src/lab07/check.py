import random  # <--- Добавьте вот эту строку
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        
        result = fn(nums)
        
        # Проверка, что отсортировали правильно
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: получилось {result}"
        # Проверка, что исходный список не изменился
        assert nums == original, f"{fn.__name__} изменила исходный список!"

def check_search():
    for _ in range(50):
        nums = [random.randint(-20, 20) for _ in range(random.randint(0, 30))]
        x = random.randint(-20, 20)
        
        # --- Тест линейного поиска ---
        try:
            expected_linear = nums.index(x)
        except ValueError:
            expected_linear = -1
            
        res_linear = linear_search(nums, x)
        assert res_linear == expected_linear, f"linear_search ошибся на {nums} для {x}: {res_linear} != {expected_linear}"
        
        # --- Тест бинарного поиска ---
        sorted_nums = sorted(nums)
        res_bin = binary_search(sorted_nums, x)
        
        # Проверяем, есть ли x в исходном списке
        if x not in nums:
            assert res_bin == -1, f"binary_search должен был вернуть -1 для {x} на {sorted_nums}, но вернул {res_bin}"
        else:
            assert res_bin != -1, f"binary_search не нашел {x} на {sorted_nums}"
            # Главная проверка: по индексу res_bin в отсортированном списке должен лежать x
            assert sorted_nums[res_bin] == x, f"binary_search вернул неверный индекс {res_bin} (там {sorted_nums[res_bin]}) для {x} на {sorted_nums}"

    # Тесты крайних случаев
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1
    assert binary_search([], 5) == -1

def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(2, 20)
        nums = [random.randint(-50, 50) for _ in range(n)]
        
        # Генерируем target, который точно есть в списке
        if n >= 2:
            i, j = random.sample(range(n), 2)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-100, 100)
            
        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        
        # Оба должны найти пару или оба вернуть None
        assert (res_brute is None and res_fast is None) or (res_brute is not None and res_fast is not None), \
            f"Расхождение на {nums} с target={target}. Brute: {res_brute}, Fast: {res_fast}"
            
        # Если нашли, проверяем сумму
        if res_brute:
            i, j = res_brute
            assert nums[i] + nums[j] == target, f"Brute вернул неверные индексы: {res_brute}"
            i, j = res_fast
            assert nums[i] + nums[j] == target, f"Fast вернул неверные индексы: {res_fast}"

if __name__ == "__main__":
    random.seed(42)
    
    # Считаем количество проверок для вывода
    n_trials = 100
    
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn, trials=n_trials)
        
    check_search()
    check_two_sum(trials=n_trials)
    
    print(f"OK: {n_trials * 3 + 50 + n_trials} проверок пройдено без ошибок.")