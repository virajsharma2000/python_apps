def call_counter(func):
    func.call_count = 0  # Add a custom attribute to the function

    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} times")
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper

@call_counter
def my_function():
    pass

my_function()
my_function()
# Output:
