def counter(start, stop):
    i = start
    while i <= stop:
        yield i  # Pause and return current value
        i += 1

for num in counter(1, 10):
    print(num)  # Output: 1 2 3 4 5 6 7 8 9 10

