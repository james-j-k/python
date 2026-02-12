def decorator(fun):
    def wrapper(*args,**kwargs):
        print("Before executing the function")
        fun(*args,**kwargs)
        print("After executing the function")
    return wrapper

@decorator
def add(a,b):
    print(a+b)

add(2,4)