from ReverseIterator import ReverseIterator
from SequenceDoubleIterator import SequenceDoubleIterator
from SequenceStringIterator import SequenceStringIterator
from AlternatingIterator import AlternatingIterator
from SkippingElementIterator import SkippingElementIterator


def multiples_of_num(num):
    """ Generator function that yields multiples of the given number indefinitely.
        Parameters: num (int): The number for which multiples are to be generated.
        Yields: int: The next multiple of the given number. """
    m = 1
    while True:
        yield m * num
        m += 1


def multiples_of_4():
    _multiple = int(input("Enter the number to multiply :"))
    input_n = int(input("Enter how many times the multiplications should happen :"))
    multiple_4 = multiples_of_num(_multiple)
    for i in range(input_n):
        print(next(multiple_4))


def reversing_list():
    inp_list_2 = list(map(int, input("Enter the list of integers with space to reverse :").split()))
    for i in ReverseIterator(inp_list_2):
        print(i)


def generate_even_num():
    limit = int(input("Enter the limit :"))
    even_nums = multiples_of_num(2)
    for i in range(limit):
        print(next(even_nums))


def double_list_values():
    inp_list_4 = list(map(int, input("Enter the list of integers with space to double :").split()))
    for doubled_value in SequenceDoubleIterator(inp_list_4):
        print(doubled_value)


def gen_word_len_from_sentence():
    inp_string = input("Enter the Sentence :")
    for word_lengths in SequenceStringIterator(inp_string):
        print(word_lengths)


def sliding_window_sum():
    def sliding_window(size, l1):
        for i in range(len(l1) - size + 1):
            j = i + size
            print(sum(l1[i:j]))

    k = int(input("Enter the size to sum:"))
    l1 = list(map(int, input("Enter the list of integers with space for sliding window :").split()))
    sliding_window(k, l1)


def alternate_list_values():
    alternate_lst1 = list(map(int, input("Enter the values of alternate list1 with space :").split()))
    alternate_lst2 = list(map(int, input("Enter the values of alternate list2 with space :").split()))
    alternated_elements = AlternatingIterator(alternate_lst1, alternate_lst2)
    for i in alternated_elements:
        print(i)


def skip_third_element():
    skip_third_element_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    skipped_elements = SkippingElementIterator(skip_third_element_lst)
    for i in skipped_elements:
        print(i)


def gen_cumulative_products():
    def cumulative_products(l):
        n = 0
        m = l[n]
        while True:
            yield l[n] * m
            m *= l[n]
            n += 1

    l = [1, 2, 43, 5]
    li = cumulative_products(l)
    for i in range(len(l)):
        print(next(li))


multiples_of_4()
reversing_list()
generate_even_num()
double_list_values()
gen_word_len_from_sentence()
sliding_window_sum()
alternate_list_values()
skip_third_element()
gen_cumulative_products()