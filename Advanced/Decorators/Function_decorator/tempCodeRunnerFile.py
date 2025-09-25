
def try_decorator(func):
    def function():
        print("hello")
        func()
        print("bye")
    return function
@try_decorator
def display():
    print("kartik")
    