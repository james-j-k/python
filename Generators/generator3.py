num = int(input())
def read_numbers():
    for i in range(num):
        yield i

def square(numbers):
    for n in numbers:
        yield n * n

def even_only(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

pipeline = even_only(square(read_numbers()))

for value in pipeline:
    print(value)
