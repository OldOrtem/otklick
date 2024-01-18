import random
import time
"""
Для решения данной задачи оптимальным выбором может быть алгоритм сортировки,
называемый Timsort. Этот алгоритм был разработан Тимом Петерсом
для использования в языке программирования Python. Timsort сочетает в себе
сортировку вставками и сортировку слиянием, что позволяет ему эффективно
обрабатывать различные виды входных данных.

Преимущества Timsort:
Эффективность в обработке случайных данных.
Использует сортировку вставками, которая хорошо работает на почти упорядоченных данных.
Эффективность в обработке данных с повторяющимися элементами.
Эффективность на больших объемах данных: Сортировка слиянием позволяет эффективно сортировать большие массивы данных.
"""

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, left, mid, right):
    len_left = mid - left + 1
    len_right = right - mid

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

if __name__ == "__main__":

    array = [random.randint(1, 100) for _ in range(100000)]

    array1 = array.copy()
    array2 = array.copy()

    start1 = time.time()
    timsort(array1)
    end1 = time.time()

    start2 = time.time()
    array2.sort()
    end2 = time.time()

    print(array1 == array2)
    print(end1 - start1, end2 - start2)