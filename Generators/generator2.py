def count_up_to(max_value):
    current = 0
    while current < max_value:
        current += 1
        yield current
for num in count_up_to(5):
    print(num)
