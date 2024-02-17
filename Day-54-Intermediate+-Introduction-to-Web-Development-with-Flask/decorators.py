import time


def function_decorator(function):
    def wrapper_function():
        function()
        time.sleep(2)
        function()
        print('Voila!')
        function()

    return wrapper_function


@function_decorator
def say_hello():
    print('Hello World!')


if __name__ == '__main__':
    say_hello()