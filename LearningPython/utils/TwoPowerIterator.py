import math


class TwoPowerIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sequence):
            item = int (math.pow(2, self.sequence[self.index]))
            self.index += 1
            return item
        else:
            raise StopIteration
