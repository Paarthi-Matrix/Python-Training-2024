# 2,7
def even_no(n):
    """
    Generate the first 'n' even numbers starting from 0.

    Args:
        n (int): The number of even numbers to generate.

    Yields:
        int: The next even number.
    """
    num = 0
    while n >= 1:
        yield num
        num += 2
        n -= 1


# 4
def square_no(n):
    """
    Generate the first 'n' square numbers.

    Args:
        n (int): The number of square numbers to generate.

    Yields:
        int: The next square number.
    """
    num = 1
    while n > 0:
        yield num * num
        num += 1
        n -= 1


# 6
def generate_no(n):
    """
    Generate the first 'n' natural numbers starting from 1.

    Args:
        n (int): The number of natural numbers to generate.

    Yields:
        int: The next natural number.
    """
    num = 1
    while n > 0:
        yield num
        num += 1
        n -= 1


# 12
def multiples_of_no(m, n):
    """
    Generate the first 'n' multiples of a given number 'm'.

    Args:
        m (int): The number to generate multiples of.
        n (int): The number of multiples to generate.

    Yields:
        int: The next multiple of 'm'.
    """
    while n > 0:
        yield m * n
        n -= 1


# 11
def factorial_num(n):
    """
    Generate the factorial sequence up to 'n!'.

    Args:
        n (int): The maximum factorial to generate.

    Yields:
        int: The next factorial value.
    """
    fact = 1
    res = 1
    while fact <= n:
        res *= fact
        yield res
        fact += 1


# 9
def repeat_elements(ls):
    """
    Generate each element in the list, repeating each element 'k' times
    where 'k' is the element's position in the list.

    Args:
        ls (list): The list of elements to repeat.

    Yields:
        object: The next element in the sequence.
    """
    k = 0
    while k < len(ls):
        for _ in range(k + 1):
            yield ls[k]
        k += 1


# 2
values = even_no(2)
for i in values:
    print(i)

# 4
sqr_no = square_no(5)
for i in sqr_no:
    print(i)

# 6
numbers = generate_no(10)
for i in numbers:
    print(i)

# 7
ls = [10, 20, 30, 40, 50, 60, 70]
index = 0
if len(ls) % 2 != 0:
    index = len(ls) / 2 + 1
else:
    index = len(ls) / 2

even_index = even_no(index)
for i in even_index:
    print(ls[i])

# 9
repeats = repeat_elements(['a', 'b', 'c', 'd', 'e'])
for i in repeats:
    print(i, end=" ")

# 11
fact_no = factorial_num(5)
for i in fact_no:
    print(i, end=" ")

# 12
multiples = multiples_of_no(3, 4)
for i in multiples:
    print(i, end=" ")
