from utils.AlternateIterator import AlternateIterator
from utils.CumulativeSumIterator import CumulativeSumIterator
from utils.CombinationIterator import CombinationIterator
from utils.GeneratorUtils import cumulative_product_generator
from utils.GeneratorUtils import generate_combinations
from utils.GeneratorUtils import get_generator_over_list
from utils.GeneratorUtils import get_square_root_over_list
from utils.GeneratorUtils import merge_list_generator
from utils.GeneratorUtils import cumulative_sum_with_sliding_window_generator
from utils.TwoPowerIterator import TwoPowerIterator


def print_list_with_generator_by_index(element_list):
    """
    This function prints the element from the given list based on their index or position.
    Input: lst = ['a', 'b', 'c']. Output: a, b, b, c, c, c.

    Parameters:
        element_list (list) : list of elements. The list may contain any valid values or python literals.

    """

    list_gen = get_generator_over_list(element_list)
    for index, val in list_gen:
        while index >= 0:
            print(val)
            index -= 1


def get_cumulative_sum_of_list(number_list):
    """
    This function prints the cumulative sums for given list.
    Input: lst = [10, 20, 30]. Output: 10, 30, 60.

    Parameters:
        number_list (list) : list of integers or float. MUST CONTAIN ONLY INTEGERS OR FLOATS

    """

    for number in CumulativeSumIterator(number_list):
        print(number)


def generate_square_root(number_list):
    """
    This function prints square roots of given list of integers.
    Input: lst = [1, 4, 9, 16]. Output: 1.0, 2.0, 3.0, 4.0.

    Parameters:
        number_list (list) = list of integers. THE LIST MUST ONLY CONTAIN INTEGERS
    """

    for number in get_square_root_over_list(number_list):
        print(number)


def generate_two_powers_by_range(n):
    """
    This function prints the powers of 2 up to n terms.
    Input: n = 4. Output: 1, 2, 4, 8.

    Parameters:
        n (int) : Range upto which the powers of 2 need to be calculated.
                  MUST BE INTEGER ONLY.
    """

    for num in TwoPowerIterator(range(0, n)):
        print(num)


def generate_combinations_of_two_list(list_1, list_2):
    """
    This function returns the list that have the combinations of 2 given list.
    Input: lst1 = [1, 2], lst2 = ['a', 'b']. Output: (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b').

    Parameters:
        list_1 (list) : List of elements
        list_2 (list) : List of elements

    Returns:
        answer (list) : Contains the combination of given input lists.
    """

    answer = []
    for element_1, element_2 in generate_combinations(list_1, list_2):
        answer.append((element_1, element_2))
    return answer


def generate_combinations_on_list_by_N(num_list, length):
    """
     This function generates combinations of length N from input list.
     Input: lst = [1, 2, 3], length = 2. Output: (1, 2), (1, 3), (2, 3).

     Parameters:
         num_list (list) : list of elements to generate the combinations.
         length (int) : This represents the length of each combination.

     """

    for list in CombinationIterator(num_list, length):
        print(list)


def merge_list(list_1, list_2):
    """
    This function merges the sorted lists and print them in sorted order.

    Parameters:
        list_1 (list)
        list_2 (list)
    """

    for num in merge_list_generator(list_1, list_2):
        print(num)


def get_cumulative_product_of_list(number_list):
    """
    This function returns the list of cumulative products of given list.
    """

    answer = []
    for num in cumulative_product_generator(number_list):
        answer.append(num)
    return answer


def get_alternate_elements_of_list(list_1, list_2):
    """
    This function returns the alternate elements between the given two lists
    """

    for item in AlternateIterator(list_1, list_2):
        print(item)


def get_sum_of_list_by_window_size(number_list, window_size):
    """
    This function returns the cumulative sliding window sums of size N from given list.

    Parameters:
        number_list (list) : list of integers or float
        window_size (int) : This represents the sliding window size.
                            Make sure that always windows size is less than length of given list.
    """

    answer = []
    for num in cumulative_sum_with_sliding_window_generator(number_list, window_size):
        answer.append(num)
    return answer


element_list = ['a', 'b', 'c', 'd']
number_list = [1, 4, 9, 16]
num_list = [1, 2, 3, 5, 4]
lst1 = [1, 2, "s"]
lst2 = ['a', 'b', 1]
list_1 = [1, 4]
list_2 = [2, 3, 9]
print_list_with_generator_by_index(element_list)  # 1
print()
get_cumulative_sum_of_list(number_list)  # 2
print()
generate_square_root(number_list)  # 3
print()
generate_two_powers_by_range(5)  # 4
print()
print(generate_combinations_of_two_list(lst1, lst2))  # 5
print()
print(get_sum_of_list_by_window_size(number_list, 2))  # 7
print()
get_alternate_elements_of_list(list_1, list_2)  # 8
print()
number_list = [1, 4, 9, 16]
print(get_cumulative_product_of_list(number_list))  # 9
print()
merge_list(list_1, list_2)  # 10
print()
generate_combinations_on_list_by_N(num_list, 2)  # 11
