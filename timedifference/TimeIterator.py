class TimeIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.sequence):
            raise StopIteration
        value = self.sequence[self.count]
        self.count += 1
        return value
