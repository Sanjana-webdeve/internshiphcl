def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        original_function()
        print("Wrapper executed after", original_function.__name__)
    return wrapper_function

@decorator_function  # This is the decorator
def say_hello():
    print("Hello!")

say_hello()
