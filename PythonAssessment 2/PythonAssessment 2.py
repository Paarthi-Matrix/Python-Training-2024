from AlternatingIterator import AlternatingIterator
from ReverseIterator import ReverseIterator
from SequenceDoubleIterator import SequenceDoubleIterator
from SequenceStringIterator import SequenceStringIterator
from SkippingElementIterator import SkippingElementIterator


def multiples_of_num(num):
    """Generator function that yields multiples of the given number indefinitely.

    This function uses a generator to yield successive multiples of a provided integer `num`.
    It starts with 1 * num and increments the multiplier by 1 each time the generator is called.

    Parameters:
        num (int): The number for which multiples are to be generated.

    Yields:
        int: The next multiple of the given number.
    """
    multiple = 1
    while True:
        yield multiple * num
        multiple += 1


def multiples_of_4():
    """Generates and prints multiples of a user-provided number for a specified count.

    This function prompts the user for a number and a count. It then generates multiples of
    the input number up to the specified count using the `multiples_of_num` generator function.
    The multiples are printed to the console.

    Example:
        If the user inputs 3 for the number and 5 for the count, the output will be:
        3, 6, 9, 12, 15
    """
    multiple = int(input("Enter the number to multiply: "))
    count = int(input("Enter how many times the multiplications should happen: "))
    multiples_generator = multiples_of_num(multiple)
    for _ in range(count):
        print(next(multiples_generator))


def reversing_list():
    """Reverses and prints a list of integers provided by the user.

    This function prompts the user to input a list of integers separated by spaces. It then
    uses the `ReverseIterator` to print each element of the list in reverse order.

    Example:
        If the user inputs "1 2 3 4", the output will be:
        4, 3, 2, 1
    """
    inp_list = list(map(int, input("Enter the list of integers with space to reverse: ").split()))
    for item in ReverseIterator(inp_list):
        print(item)


def generate_even_numbers():
    """Generates and prints even numbers up to a user-specified limit.

    This function prompts the user for a limit and then generates even numbers starting from 2
    up to the specified limit using the `multiples_of_num` generator function. Each even number
    is printed to the console.

    Example:
        If the user inputs 5, the output will be:
        2, 4, 6, 8, 10
    """
    limit = int(input("Enter the limit: "))
    even_nums = multiples_of_num(2)
    for _ in range(limit):
        print(next(even_nums))


def double_list_values():
    """Doubles each integer in a list provided by the user and prints the results.

    This function prompts the user to input a list of integers separated by spaces. It then uses
    the `SequenceDoubleIterator` to double each value in the list and print the results.

    Example:
        If the user inputs "1 2 3", the output will be:
        2, 4, 6
    """
    inp_list = list(map(int, input("Enter the list of integers with space to double them: ").split()))
    for doubled_value in SequenceDoubleIterator(inp_list):
        print(doubled_value)


def generate_word_lengths():
    """Prints the length of each word in a user-provided sentence.

    This function prompts the user for a sentence and then uses the `SequenceStringIterator`
    to calculate and print the length of each word in the sentence.

    Example:
        If the user inputs "Sriram Baskaran", the output will be:
        6, 8
    """
    inp_string = input("Enter the sentence: ")
    for word_length in SequenceStringIterator(inp_string):
        print(word_length)


def sliding_window(size, input_list):
    """
    Calculates the sum of all possible sliding windows of a specified size within the input list.

    Parameters:
    size (int): The size of the sliding window.
    input_list (list): The list of numbers to process.

    Returns:
    None: Prints the sum of each sliding window to the console.

    Example:
    sliding_window(3, [1, 2, 3, 4, 5])
    Output:
    6
    9
    12
    """
    for i in range(len(input_list) - size + 1):
        window_sum = i + size
        print(sum(input_list[i:window_sum]))


def sliding_window_sum():
    """Calculates and prints the sum of elements in sliding windows of a user-specified size.

    This function prompts the user to input a list of integers and a window size. It then calculates
    the sum of elements within each sliding window of the specified size and prints the sums.

    Example:
        If the user inputs "1 2 3 4 5" for the list and 3 for the size, the output will be:
        6, 9, 12
    """
    window_size = int(input("Enter the size to sum: "))
    input_list = list(map(int, input("Enter the list of integers with space for sliding window: ").split()))
    sliding_window(window_size, input_list)


def alternate_list_values():
    """Prints elements alternately from two user-provided lists of integers.

    This function prompts the user to input two lists of integers separated by spaces. It then uses
    the `AlternatingIterator` to print elements alternately from each list.

    Example:
        If the user inputs "1 2 3" for the first list and "4 5 6" for the second list,
        the output will be:
        1, 4, 2, 5, 3, 6
    """
    input_list1 = list(map(int, input("Enter the values of alternate list1 with space: ").split()))
    input_list2 = list(map(int, input("Enter the values of alternate list2 with space: ").split()))
    alternated_elements = AlternatingIterator(input_list1, input_list2)
    for element in alternated_elements:
        print(element)


def skip_third_element():
    """Prints elements of a list while skipping every third element.

    This function creates a sample list of integers from 1 to 9. It then uses the
    `SkippingElementIterator` to print the elements of the list while skipping every third element.

    Example:
        The output for the default list will be:
        1, 2, 4, 5, 7, 8
    """
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    skipped_elements = SkippingElementIterator(sample_list)
    for element in skipped_elements:
        print(element)


def cumulative_products(input_list):
    """
    Generates cumulative products of elements in the input list. The cumulative product at each
    position is the product of all elements in the list up to that position.

    Parameters:
    input_list (list): The list of numbers to process.

    Yields:
    int: The cumulative product at each step.

    Example:
    list(cumulative_products([1, 2, 3, 4]))
    Output:
    [1, 2, 6, 24]
    """
    index = 0
    product = input_list[index]
    while True:
        yield input_list[index] * product
        product *= input_list[index]
        index += 1


def generate_cumulative_products():
    """Calculates and prints the cumulative products of elements in a list.

    This function defines a helper generator function `cumulative_products` that calculates the
    cumulative product of elements in a list. It starts with the first element and multiplies it
    by the next element iteratively, printing each cumulative product.

    Example:
        For the sample list [1, 2, 43, 5], the output will be:
        1, 2, 86, 430
    """

    sample_list = [1, 2, 43, 5]
    cumulative_generator = cumulative_products(sample_list)
    for _ in range(len(sample_list)):
        print(next(cumulative_generator))


if __name__ == "__main__":
    multiples_of_4()
    reversing_list()
    generate_even_numbers()
    double_list_values()
    generate_word_lengths()
    sliding_window_sum()
    alternate_list_values()
    skip_third_element()
    generate_cumulative_products()
