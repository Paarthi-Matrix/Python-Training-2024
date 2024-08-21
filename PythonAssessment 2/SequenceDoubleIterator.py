class SequenceDoubleIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.sequence):
            raise StopIteration
        self.current += 1
        return self.sequence[self.current - 1] * 2
