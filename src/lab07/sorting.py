def bubble_sort(nums: list) -> list:
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""
    # Создаем копию, чтобы не менять исходный список (как учили в Л3)
    arr = list(nums)
    n = len(arr)
    
    for i in range(n):
        swapped = False
        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Оптимизация: если обменов не было, список уже отсортирован
        if not swapped:
            break
    return arr

def insertion_sort(nums: list) -> list:
    """Тот же контракт, что у bubble_sort."""
    arr = list(nums)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвигаем элементы больше key на одну позицию вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(nums: list) -> list:
    """Тот же контракт, что у bubble_sort."""
    arr = list(nums)
    n = len(arr)
    for i in range(n):
        # Ищем минимальный элемент в оставшейся части
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами текущий и найденный минимальный
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr