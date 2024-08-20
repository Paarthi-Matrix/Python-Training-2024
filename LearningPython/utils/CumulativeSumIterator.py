class CumulativeSumIterator:

    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0
        self.cumulative_sum = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sequence):
            self.cumulative_sum += self.sequence[self.index]
            self.index += 1
            return self.cumulative_sum
        else:
            raise StopIteration
