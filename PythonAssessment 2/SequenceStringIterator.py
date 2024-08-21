class SequenceStringIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.d_list = self.sequence.split()
        if self.current >= len(self.d_list):
            raise StopIteration
        self.current += 1
        return len(self.d_list[self.current - 1])
