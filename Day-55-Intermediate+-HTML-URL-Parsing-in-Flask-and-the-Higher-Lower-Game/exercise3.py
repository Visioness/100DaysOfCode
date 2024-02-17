inputs = eval(input())


def logging_decorator(func):
    def wrapped_function(*args):
        print(f'You called {func.__name__}{args}\nIt returned: {func(args[0], args[1], args[2])}')
    
    return wrapped_function

@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])