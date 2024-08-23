# 3
class SequenceIterator:
    """
    An iterator that iterates over the characters in a string.

    Attributes:
        _string (str): The string to iterate over.
        _index (int): The current index in the string.
    """

    def __init__(self, string):
        """
        Initializes the iterator with a string.

        Args:
            string (str): The string to iterate over.
        """
        self._string = string
        self._index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            SequenceIterator: The iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next character in the string.

        Returns:
            str: The next character in the string.

        Raises:
            StopIteration: When the end of the string is reached.
        """
        if self._index < len(self._string):
            item = self._string[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


# 3
string = input("Enter the String")
for e in SequenceIterator(string):
    print(e)


# 5
class ReverseIterator:
    """
    An iterator that iterates over a list in reverse order.

    Attributes:
        _data (list): The list to iterate over.
        _index (int): The current index in the reversed list.
    """

    def __init__(self, data):

        """
        Initializes the iterator with a list.

        Args:
            data (list): The list to iterate over.
        """
        self._data = data
        self._index = -1

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            SequenceIterator: The iterator object itself.
        """
        return self

    def __next__(self):
        """

        Returns the integer in the list of reversed order.

        Returns:
            int: integer in the reverse order.

        Raises:
            stopIteration: When the end of the string is reached.
        """
        x = -len(self._data)
        if self._index >= x:
            item = self._data[self._index]
            self._index -= 1
            return item
        else:
            raise StopIteration


# 5
ls = input("Enter the sequence").split()
print(ls)
for e in ReverseIterator(ls):
    print(e)


# 8
class StepIterator:
    """

    An iterator that iterates over a list a specified number of times,
    wrapping around if the end of the list is reached.

    Attributes:
        _l (list): The list to iterate over.
        _index (int): The current index in the iteration step.
        _k (int): The current index in the list.
        _step (int): The number of iterations before raising StopIteration.

    Methods:
        __iter__(): Returns the iterator object itself.
        __next__(): Returns the next item from the list or raises StopIteration.
    """

    def __init__(self, l, step):
        """
        Initializes the StepIterator with a list and a step count.

        Args:
            l (list): The list to iterate over.
            step (int): The number of iterations before stopping.
        """
        self._l = l
        self._index = 0
        self._k = 0
        self._step = step

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """
        Returns the next item from the list, wrapping around if necessary.

        Raises:
            StopIteration: If the specified number of iterations is reached.
        """
        if self._index < self._step:
            item = self._l[self._k]
            self._index += 1
            self._k += 1
            if self._k == len(self._l):
                self._k = 0

            return item
        else:
            raise StopIteration


# 8
ls = ['red', 'green', 'blue']
n = 6
for i in StepIterator(ls, n):
    print(i, end=" ")


# 10
class CumulativeSum:
    """
    An iterator that returns the cumulative sum of a list of numbers.

    Attributes:
         _l (list): The list of numbers to iterate over.
         _index (int): The current index in the list.
                _sum (int/float): The cumulative sum of the elements iterated over so far.

    Methods:
        __iter__(): Returns the iterator object itself.
        __next__(): Returns the next cumulative sum or raises StopIteration.
    """

    def __init__(self, l):
        """
        Initializes the CumulativeSum with a list of numbers.

        Args:
            l (list): The list of numbers to compute the cumulative sum.
        """
        self._l = l
        self._index = 0
        self._sum = 0

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """
        Returns the next cumulative sum of the list.

        Raises:
            StopIteration: If the end of the list is reached.
        """
        if self._index < len(self._l):
            self._sum = self._l[self._index] + self._sum
            self._index += 1

            return self._sum
        else:
            raise StopIteration


# 10
for i in CumulativeSum([1, 2, 3, 4, 5]):
    print(i, end=" ")
