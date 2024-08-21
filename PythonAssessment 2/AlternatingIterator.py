class AlternatingIterator:
    def __init__(self, sequence1, sequence2):
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.sequence1_index = 0
        self.sequence2_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.sequence1_index < len(self.sequence1) and self.sequence2_index < len(self.sequence2):
            if self.sequence1_index == self.sequence2_index:
                value = self.sequence1[self.sequence1_index]
                self.sequence1_index += 1
            else:
                value = self.sequence2[self.sequence2_index]
                self.sequence2_index += 1
            return value
        elif self.sequence1_index < len(self.sequence1):
            value = self.sequence1[self.sequence1_index]
            self.sequence1_index += 1
            return value
        elif self.sequence2_index < len(self.sequence2):
            value = self.sequence2[self.sequence2_index]
            self.sequence2_index += 1
            return value
        else:
            raise StopIteration
