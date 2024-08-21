# 3
class SequenceIterator:
    def __init__(self, str):
        self._str = str
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._str):
            item = self._str[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


# 3
str = input("Enter the String")
for e in SequenceIterator(str):
    print(e)


# 5
class ReverseIterator:
    def __init__(self, ls):
        self._ls = ls
        self._index = -1

    def __iter__(self):
        return self

    def __next__(self):
        x = -len(self._ls)
        if self._index >= x:
            item = self._ls[self._index]
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
    def __init__(self, l, step):
        self._l = l
        self._index = 0
        self._k = 0
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
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
    def __init__(self, l):
        self._l = l
        self._index = 0
        self._sum = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._l):
            self._sum = self._l[self._index] + self._sum
            self._index += 1

            return self._sum
        else:
            raise StopIteration


# 10
for i in CumulativeSum([1, 2, 3, 4, 5]):
    print(i, end=" ")
