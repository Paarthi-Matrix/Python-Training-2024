"""
__iter__():

* It is a method.
* It returns the iterator object itself.
* It is used when a custom iterator for iterating is needed.


__next__():
* It is also a method.
* It returns the next value of the object.
* It raises stopIterator exception if there is no next value after start, end point that is set.
* ie : if there is no more value to iterate it after
"""


class NumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


if __name__ == '__main__':
    num_iterator = NumberIterator(10, 15)
    for numbers in num_iterator:
        print(numbers)
