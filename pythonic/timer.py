from time import perf_counter

class Timer:
    def __init__(self, label):
        self.label = label
    def __enter__(self):
        self.start = perf_counter()
    def __exit__(self, type, value, traceback):
        print(f'{self.label}: {(perf_counter()-self.start):0.4f}')
