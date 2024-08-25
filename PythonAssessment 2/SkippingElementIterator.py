class SkippingElementIterator:
    """
    An iterator that skips every third element in the sequence.

    Attributes:
    sequence (iterable): The sequence to be iterated over.
    index (int): The current index position in the sequence.
    """

    def __init__(self, sequence):
        """
        Initializes the SkippingElementIterator with a sequence.

        Parameters:
        sequence (iterable): The sequence to iterate over.
        """
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
        SkippingElementIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next element in the sequence, skipping every third element.

        Returns:
        element: The next element in the sequence that is not skipped.

        Raises:
        StopIteration: If there are no more elements to return.
        """
        while self.index < len(self.sequence):
            value = self.sequence[self.index]
            self.index += 1
            if self.index % 3 == 0:
                continue
            return value

        raise StopIteration