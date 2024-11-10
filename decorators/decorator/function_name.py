def conditional_decorator(func):
    def wrapper(*args, **kwargs):
        if func.__name__.startswith("test") or func.__name__.endswith("test"):
            print("Special handling for test functions")
        else:
            print("Standard handling")

        func(*args, **kwargs)

    return wrapper

@conditional_decorator
def test_function():
    print("This is a test function.")

@conditional_decorator
def regular_function():
    print("This is a regular function.")

test_function()
# Output:
# Special handling for test functions
# This is a test function.

regular_function()
# Output:
# Standard handling
# This is a regular function.
