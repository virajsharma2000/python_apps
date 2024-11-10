def one_time_use(func):
    func.has_been_called = False

    def wrapper(*args, **kwargs):
        if wrapper.has_been_called:
            raise Exception(f"{func.__name__} can only be called once!")
        wrapper.has_been_called = True
        return func(*args, **kwargs)

    wrapper.has_been_called = False
    return wrapper

@one_time_use
def initialize():
    print("Initialization complete.")

initialize()  # Works the first time
initialize()  # Raises an Exception: "initialize can only be called once!"
