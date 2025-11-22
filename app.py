def decorator(func):
    def wrapper():
        print("before execution")
        func()
        print("After execution")
    return wrapper
@decorator    
def say_hello():
    print("Hello Nikhil")
say_hello()           