class SequenceDoubleIterator:
    """
    An iterator that iterates over a sequence and returns each element doubled.

    Attributes:
    sequence (iterable): The sequence to be iterated over.
    current (int): The current index position in the sequence.
    """

    def __init__(self, sequence):
        """
        Initializes the SequenceDoubleIterator with a sequence.

        Parameters:
        sequence (iterable): The sequence to iterate over.
        """
        self.sequence = sequence
        self.current = 0

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
        SequenceDoubleIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next element in the sequence, each element doubled.

        Returns:
        element: The next element in the sequence, doubled.

        Raises:
        StopIteration: If there are no more elements to return.
        """
        if self.current >= len(self.sequence):
            raise StopIteration
        self.current += 1
        return self.sequence[self.current - 1] * 2

