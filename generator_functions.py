def odd_generator(threshold):
    """Write a generator for the first 4 odd numbers. Input: n = 4. Output: 1, 3, 5, 7."""

    count = 0
    value = 1
    while count <= threshold:
        yield value
        value += 2
        count += 1


odd_nums = odd_generator(4)
for num in odd_nums:
    print(num)


def fibonacci_generator(threshold):
    """Generate the Fibonacci sequence up to 4 terms. Input: n = 4. Output: 0, 1, 1, 2."""

    base_1 = 0
    base_2 = 1
    count = 0
    while count <= threshold:
        fib_num = base_1
        base_1, base_2 = base_2, base_1 + base_2
        count += 1
        yield fib_num


fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num)


def factorial(num):
    """Creating a generator for factorial values from 1 to 3. Input: n = 3. Output: 1, 2, 6."""

    if num == 1 or num == 0:
        return 1
    elif num < 1:
        return 'Enter the values in positive number'
    else:
        return num * factorial(num-1)


def factorial_generator(values):
    for value in range(1, values+1):
        yield factorial(value)


n = 3
gen = factorial_generator(3)
for factorial_value in gen:
    print(factorial_value)


def power_of_three(threshold):
    """Design a generator for the sequence of powers of 3 up to 5 terms. Input: n = 5. Output: 1, 3, 9, 27, 81."""

    count = 0
    while count < threshold:
        term = count
        count += 1
        yield 3 ** term


pow_three = power_of_three(5)
for value in pow_three:
    print(value)


def flatten_list(input_list):
    """Write a generator that flattens the nested list [[1, 2], [3, 4], [5, 6]].
    Input: nested_list = [[1, 2], [3, 4], [5, 6]]. Output: 1, 2, 3, 4, 5, 6."""

    flat_list = list()
    for each in input_list:
        flat_list.extend(each)
    return flat_list


nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = list(flatten_list(nested_list))
for value in flattened_list:
    print(value, end='\t')


def unique_permutations(list_input, depth=0):
    """Write a generator for unique permutations of [1, 2]. Input: lst = [1, 2]. Output: (1, 2), (2, 1)."""
    if depth >= len(list_input):
        print(list_input)
        return
    for num in range(depth, len(list_input)):
        list_input[depth], list_input[num] = list_input[num], list_input[depth]
        unique_permutations(list_input, depth+1)
        list_input[depth], list_input[num] = list_input[num], list_input[depth]


def unique_permutations_new(list_input):
    if len(list_input) == 1:
        yield (list_input[0],)
    unique_elements = set(list_input)
    for element in unique_elements:
        remaining_element = list(list_input)
        remaining_element.remove(element)
        for permutation in unique_permutations_new(remaining_element):
            yield (element,) + permutation


lst = [1, 2]
permute = unique_permutations_new(lst)
for per in permute:
    print(per)






