def execution_logger(func):
    def wrapper(*args):
        print(f"Starting Execution of {func.__name__}")
        result = func(*args)   
        print(f"Completed Execution of {func.__name__}")
        return result         
    return wrapper

@execution_logger
def prod(a,b):
    return a*b

result = prod(5,4)
print("Result: ", result)
