from timer import Timer

N = 10_000_000

some_vector = range(N)

with Timer('Explicit indexing'):
    total = 0
    for i in range(N):
        total += some_vector[i]

# with Timer('Zip'):
#     total = 0
#     for x in some_vector:
#         total += x 

# with Timer('Sum'):
#     total = sum(some_vector)