import time
# Опциональное  задание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера;
class Stopwatch: # класс секундомер
    def __init__(self, func, num_runs=100): # num_runs - количество итераций запуска функции
        self.func = func # выполняемая функция
        self.num_runs = num_runs

    def __call__(self, *args, **kwargs):
        avg_time = 0                     
        for _ in range(self.num_runs):
            t0 = time.time()
            ### <<полезный>> код, скорость которого мы оцениваем
            self.func(*args, **kwargs)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.num_runs
        print("Среднее время выполнения при %s итерациях заняло %.5f секунд" % (self.num_runs, avg_time))
        return self.func(*args, **kwargs)

@Stopwatch
def f():
    for j in range(1000000): pass # простая фунция счета до 1 000 000, обернутая в class Stopwatch
f()
