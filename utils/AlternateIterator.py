class AlternateIterator:
    def __init__(self, sequence_1, sequence_2):
        self.sequence_1 = sequence_1
        self.sequence_2 = sequence_2
        self.index = 0
        self.toggle_sequence = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence_1) or self.index >= len(self.sequence_2):
            raise StopIteration
        if self.toggle_sequence:
            self.toggle_sequence = not self.toggle_sequence
            return self.sequence_1[self.index]
        else:
            answer = self.sequence_2[self.index]
            self.toggle_sequence = not self.toggle_sequence
            self.index += 1
            return answer
