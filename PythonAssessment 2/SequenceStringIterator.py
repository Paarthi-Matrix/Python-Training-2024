class SequenceStringIterator:
    """
    An iterator that iterates over a string sequence and returns the length
    of each word in the sequence.

    Attributes:
    sequence (str): The string to be split into words and iterated over.
    current (int): The current index position in the list of words.
    d_list (list): The list of words obtained by splitting the sequence.
    """

    def __init__(self, sequence):
        """
        Initializes the SequenceStringIterator with a sequence.

        Parameters:
        sequence (str): The string to iterate over.
        """
        self.sequence = sequence
        self.current = 0
        self.d_list = self.sequence.split()

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
        SequenceStringIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the length of the next word in the sequence.

        Returns:
        int: The length of the next word in the sequence.

        Raises:
        StopIteration: If there are no more words to return.
        """
        if self.current >= len(self.d_list):
            raise StopIteration
        self.current += 1
        return len(self.d_list[self.current - 1])

