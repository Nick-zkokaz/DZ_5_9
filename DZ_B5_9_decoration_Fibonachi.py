import time
# Опциональное задание с двумя звездочками: написать декоратор в качестве объекта класса-секундомера,
# который можно использовать как контекстный менеджер.
# В юните B5.8 была задачка на последовательность Фибоначчи.
# Если увеличить верхнюю границу последовательности, то функцию, написанную в той задачке,
# можно прогнать для отладки поведения секундомера.
def time_this(num_runs): # здесь передается число запусков  как параметр.
    def decorator(func):
        def wrap(param):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                ### <<полезный>> код, скорость которого мы оцениваем
                func(param)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            return print("Среднее время по ", str(num_runs), "итерациям заняло %.5f секунд" % avg_time)
        return wrap
    return decorator


@time_this(num_runs=10)
def fibonachi(set_range):
    fib = {0: 0, 1: 1}
    sum_fib = 0
    for n in range(2, set_range):
        fib_n = fib[n-1] + fib[n-2]
        if fib_n < 4000000:
            fib[n] = fib_n
        else:
            break
        if fib_n % 2 == 0:
            sum_fib += fib_n
    return print("Последнее число, меньшее 4000000: {} \nСумма четных: {}".format(fib[n-1], sum_fib))
        

set_range = 100000000
fibonachi(set_range)
