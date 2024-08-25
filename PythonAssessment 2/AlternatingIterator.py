class AlternatingIterator:
    """Iterator to alternate between two sequences.

    This iterator yields elements from two sequences alternately. When one sequence
    is exhausted, it continues yielding elements from the remaining sequence.
    """

    def __init__(self, sequence1, sequence2):
        """Initialize the iterator with two sequences.

        Args:
            sequence1 (iterable): The first sequence to iterate over.
            sequence2 (iterable): The second sequence to iterate over.
        """
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.sequence1_index = 0
        self.sequence2_index = 0

    def __iter__(self):
        """Return the iterator object itself.

        Returns:
            AlternatingIterator: The iterator object.
        """
        return self

    def __next__(self):
        """Return the next item from the alternating sequences.

        Yields:
            object: The next item from the first or second sequence.

        Raises:
            StopIteration: When both sequences are exhausted.
        """

        if (self.sequence1_index < len(self.sequence1) and
                self.sequence2_index < len(self.sequence2)):
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