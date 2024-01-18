import time


def isEven(value):
    return value % 2 == 0
# + Простота и читаемость
# - При больших значениях не эффективно, оператор деления с остатком медленный
def is_even_alternative(value):
    return value & 1 == 0
# +Выполнение побитовых операций выполняется быстрей
# -код стал не таким очевидным и понятным, особенно для тех кто не достаточно хорошо знаком с побитовыми операциями

def measure_time(repetitions):
    start_time_func1 = time.time()

    for i in range(repetitions):
        result_func1 = isEven(i)

    end_time_func1 = time.time()

    start_time_func2 = time.time()

    for i in range(repetitions):
        result_func2 = is_even_alternative(i)

    end_time_func2 = time.time()

    return end_time_func1 - start_time_func1, end_time_func2 - start_time_func2

print(measure_time(100000000))