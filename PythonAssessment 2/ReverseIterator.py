class ReverseIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.current = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if 0 >= self.current:
            raise StopIteration
        self.current -= 1
        return self.sequence[self.current]
