class SequenceIterator:
    def __init__(self, sequence):
        if isinstance(sequence, dict):
            self.sequence = list(sequence.items())
        else:
            self.sequence = list(sequence)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sequence):
            item = self.sequence[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
