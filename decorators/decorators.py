import datetime


def decorator_func(fun):
    def wrapper_func():
        print("This is a wrapper function")
        fun()
    return wrapper_func


def print_hello():
    print("Hello")

new_func = decorator_func(print_hello)

new_func()

# Above code is equivalent to:
# @decorator_func

@decorator_func
def display_time():
    print("This is a function with decorator")
    print(datetime.datetime.now())

display_time()

