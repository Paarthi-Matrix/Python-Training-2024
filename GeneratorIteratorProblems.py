from utils.AlternateIterator import AlternateIterator
from utils.CumulativeSumIterator import CumulativeSumIterator
from utils.CombinationIterator import CombinationIterator
from utils.GeneratorUtils import cumulative_product_generator
from utils.GeneratorUtils import generate_combinations
from utils.GeneratorUtils import get_generator_over_list
from utils.GeneratorUtils import get_square_root_over_list
from utils.GeneratorUtils import merge_list_generator
from utils.TwoPowerIterator import TwoPowerIterator


def print_list_with_generator_by_index(element_list):
    """ Create a generator that repeats elements in ['a', 'b', 'c'] based on their index.
        Input: lst = ['a', 'b', 'c']. Output: a, b, b, c, c, c."""
    list_gen = get_generator_over_list(element_list)
    for index, val in list_gen:
        while index >= 0:
            print(val)
            index -= 1


def get_cumulative_sum_of_list(number_list):
    """ Write an iterator that calculates cumulative sums for [10, 20, 30].
    Input: lst = [10, 20, 30]. Output: 10, 30, 60. """
    for number in CumulativeSumIterator(number_list):
        print(number)


def generate_square_root(number_list):
    """
    Design a generator for square roots of [1, 4, 9, 16].
    Input: lst = [1, 4, 9, 16]. Output: 1.0, 2.0, 3.0, 4.0.
    """
    for number in get_square_root_over_list(number_list):
        print(number)


def generate_two_powers_by_range(n):
    """
    Create an iterator for powers of 2 up to 4 terms.
    Input: n = 4. Output: 1, 2, 4, 8.
    """
    for num in TwoPowerIterator(range(0, n)):
        print(num)


def generate_combinations_of_two_list(list_1, list_2):
    """
    Write a generator for combinations of [1, 2] and ['a', 'b'].
    Input: lst1 = [1, 2], lst2 = ['a', 'b']. Output: (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b').
    """
    answer = []
    for element_1, element_2 in generate_combinations(list_1, list_2):
        answer.append((element_1, element_2))
    return answer


def generate_combinations_on_list_by_N(num_list, length):
    for list in CombinationIterator(num_list, length):
        print(list)


def merge_list(list_1, list_2):
    for num in merge_list_generator(list_1, list_2):
        print(num)


def get_cumulative_product_of_list(number_list):
    answer = []
    for num in cumulative_product_generator(number_list):
        answer.append(num)
    return answer


def get_alternate_elements_of_list(list_1, list_2):
    for item in AlternateIterator(list_1, list_2):
        print(item)


element_list = ['a', 'b', 'c', 'd']
number_list = [1, 4, 9, 16]
num_list = [1, 2, 3]
lst1 = [1, 2, "s"]
lst2 = ['a', 'b', 1]
list_1 = [1, 4]
list_2 = [2, 3, 9]
print_list_with_generator_by_index(element_list)  # 1
get_cumulative_sum_of_list(number_list)  # 2
generate_square_root(number_list)  # 3
print()
generate_two_powers_by_range(5)  # 4
print(generate_combinations_of_two_list(lst1, lst2))  # 5
generate_combinations_on_list_by_N(num_list, 2)  # 11
merge_list(list_1, list_2)  # 10
print(get_cumulative_product_of_list(number_list))  # 9
get_alternate_elements_of_list(list_1, list_2)

