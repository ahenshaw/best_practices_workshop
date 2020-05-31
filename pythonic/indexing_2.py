from timer import Timer

N = 10_000_000

some_vector    = range(N)
another_vector = range(N)

with Timer('Explicit indexing'):
    total = 0
    for i in range(N):
        total += some_vector[i] + another_vector[i]

with Timer('Zip'):
    total = 0
    for x, y in zip(some_vector, another_vector):
        total += x + y

# with Timer('Sum of list'):
#     total = sum([(x+y) for x, y in zip(some_vector, another_vector)])

# with Timer('Sum of iterator'):
#     total = sum(((x+y) for x, y in zip(some_vector, another_vector)))