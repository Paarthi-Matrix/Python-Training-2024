class SkippingElementIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        value = self.sequence[self.index]
        if (self.index + 1) % 3 == 0:
            self.index += 1
            return self.__next__()
        self.index += 1
        return value

