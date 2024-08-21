import sys


def count_no_of_character_occurrence(input_str):
    """
    Count the number of character occurrence in a given string.

    Parameters:
    input_str (string) : Input string to be checked for character occurrence.

    Returns:
    character_occurrence (dict) : Dictionary of characters and their corresponding occurrences.
    """
    character_occurrence = {}
    if not input_str or input_str == "":
        return character_occurrence
    start = 0
    end = len(input_str) - 1
    while start <= end:
        if input_str[start] in character_occurrence:
            character_occurrence[input_str[start]] = character_occurrence[input_str[start]] + 1
        else:
            character_occurrence[input_str[start]] = 1
        if input_str[end] in character_occurrence:
            character_occurrence[input_str[end]] = character_occurrence[input_str[end]] + 1
        else:
            character_occurrence[input_str[end]] = 1
        start += 1
        end -= 1
    return character_occurrence


def get_number_of_strings_with_condition(str_list):
    """
        Returns the count of string where the string length is 2
        or more and the first and last character are same from a given list of strings.

        Parameters:
        str_list (list) : list of string.

        Returns:
        (list) : Returns the list of count and answer
                 The count represents the count of string that satisfies the condition.
                 The answer contains the list of string that satisfies the given condition.
    """
    count = 0
    answer = []
    for _str1 in str_list:
        if (len(_str1) >= 2) and (_str1[0] == _str1[len(_str1) - 1]):
            count += 1
            answer.append(_str1)
    return [count, answer]


def generate_string_form_first_and_last_char(input_str, size):
    """
    This function is used to generate a string with first N and last N of the given string.
    The N represents the size of the sub-string to be fetched form the given string
    size should be ranging from 1 to len(input_string)

    Parameters:
        input_str (string) : Input string.
        size (int) : Size of sub-string to be fetched from first and last of the given input string.

    Returns:
        answer (string) : Contains the string that satisfies the given condition.
                          Returns None if len(input_str) < size.
    """
    if len(input_str) < size:
        return None
    answer = input_str[:size] + input_str[len(input_str) - size:]
    return answer


def generate_list_of_squares(start, end):
    """
    Generates and returns the list comprehension,
    that generates a list of squares of numbers from 1 to 20.
    """
    return [num * num for num in range(start, end)]


def sort_list_by_tuple_last_element(input_list):
    """
    Returns a list, sorted in increasing order by the last element in each tuple
    from a given list of non-empty tuples.

    Parameters:
        input_list (list) : List of non-empty tuples. THE TUPLES MUST BE NON-EMPTY

    Returns:
        answer (list) : Returns the list of tuples in given sorted order.
    """
    answer = []
    last_element_dict = {}
    for element in input_list:
        last_element = element[-1]
        if last_element in last_element_dict:
            last_element_dict[last_element].append(element)
        else:
            last_element_dict[last_element] = [element]

    dict_keys = list(last_element_dict.keys())
    dict_keys.sort()
    for val in dict_keys:
        answer.append(last_element_dict[val])
    return flatten_list(answer)


def flatten_list(answer):
    """
    This function is used to flatten the given list to one dimensional list.
    """
    return [item for sublist in answer for item in sublist]


def modify_string(input_str):
    """
    This function returns the string by having the following condition.
    Adds 'ing' at the end of a given string (length should be at least 3).
    If the given string is already ends with 'ing' then add 'ly' instead.
    If the string length of the given string is less than 3, leaves it unchanged.
    """
    if len(input_str) < 3:
        return input_str
    if input_str.endswith("ing"):
        return input_str[:-3] + "ly"
    else:
        return input_str + "ing"


def find_min_max_of_list(number_list):
    """
    This function returns the largest and smallest numbers in the given list.

    Parameters:
        number_list (list) : List of integers. MUST CONTAIN ONLY INTEGERS.

    Returns:
        answer (list) : List that contains only 2 values. Min and Max.
                        If the list is empty returns [None, None]
    """
    answer = [None, None]
    if len(number_list) == 0:
        return answer
    min = sys.maxsize
    max = -sys.maxsize - 1
    for index in number_list:
        max = index if index > max else max
        min = index if index < min else min
    return min, max


def get_set_of_two_lists(list_1, list_2):
    """
    Returns a set of elements that are common to both lists
    """
    return {element for element in list_1 if element in list_2}


def get_set_of_list(str_list):
    """
    Return a set of words that appear more than once in the list.
    """
    return {word for word in str_list if str_list.count(word) > 1}


def perform_set_operations(list_1, list_2):
    """
    This function returns the union, intersection, and difference of the given set.
    """
    return {"Union": list_1 | list_2, "Intersection": list_1 & list_2, "Difference": list_1 - list_2}


def create_dict_comp(_list):
    """
    This function returns dictionary comprehension that maps each word in a list to its length.
    """
    return {len(val): val for val in _list}


def get_set_of_merged_tuple(tuple_1, tuple_2):
    resultant_tuple = tuple_1 + tuple_2
    return set(resultant_tuple)  # todo try without using in-build functions


def get_words_with_more_than_one_occurrence(word_list):
    word_dict = {}
    answer = []
    for word in word_list:
        if word in word_dict:
            answer.append(word)
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    return answer


# inputs
str_list = ["abc", "xyz", "aba", "1221", "ww", "1222e31", "1234567"]
word_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
input_str = "Pa"
input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (3, 4)]
number_list = [2, 6, 5, 7, 8, 33, 450, 1, -90]
list1 = [1, 2, 345, "name", "Paarthiban", "Mark", 90]
list2 = [2, 4, 345, "Paarthiban"]
set_1 = {'foo', 'bar', 'baz'}
set_2 = {'baz', 'qux', 'quux'}
tuple_1 = (2, 3, "Paarthiban", 4)
tuple_2 = (4, "Ranjith", 3, 9, 10)
word_list = ["Paarthi", "Ranjith", "Paarthi", "Ram", "Ranjith"]

print(count_no_of_character_occurrence(input_str))  # 1
print()
print(get_number_of_strings_with_condition(str_list))  # 2
print()
print(generate_string_form_first_and_last_char(input_str, 3))  # 3
print()
print(sort_list_by_tuple_last_element(input_list))  # 4
print()
print(modify_string(input_str))  # 5
print()
print(generate_list_of_squares(1, 21))  # 6
print()
min, max = find_min_max_of_list(number_list)  # 7
print("Minimum in list", min, " Maximum in list", max)
print()
print(get_set_of_two_lists(list1, list2))  # 8
print()
print(get_set_of_list(word_list))  # 9
print()
print(perform_set_operations(set_1, set_2))  # 10
print()
print(create_dict_comp(word_list))  # 12
print()
print(get_set_of_merged_tuple(tuple_1, tuple_2))  # 15
print()
print("word_count", get_words_with_more_than_one_occurrence(word_list))
