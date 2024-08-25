class ReverseIterator:
    """
    An iterator that iterates over a sequence in reverse order.

    Attributes:
    sequence (iterable): The sequence to be iterated in reverse.
    current (int): The current index position in the sequence.
    """

    def __init__(self, sequence):
        """
        Initializes the ReverseIterator with a sequence.

        Parameters:
        sequence (iterable): The sequence to iterate over in reverse.
        """
        self.sequence = sequence
        self.current = len(self.sequence)

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
        ReverseIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next element in the sequence in reverse order.

        Returns:
        element: The next element in the sequence.

        Raises:
        StopIteration: If there are no more elements to return.
        """
        if 0 >= self.current:
            raise StopIteration
        self.current -= 1
        return self.sequence[self.current]
