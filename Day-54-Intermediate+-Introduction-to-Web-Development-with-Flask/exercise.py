import time


current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrapper_function():
        current_time = time.time()
        func()
        print(f'{func.__name__} run speed: {time.time() - current_time}')
    
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


if __name__ == '__main__':
    fast_function()
    slow_function()