# d = {
#     'a': 1,
#     'b': 2,
#     'c': [1, 'a', 2],
#     'd': {'a': [1, 'x']},
#     'e': [{'x': 5, 'y': 'z'}]
# }
import sys


def count_no_of_character_occurrence(input_str):
    """
    Count the number of characters in a string. Go to the editor
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
    """
    count = 0
    answer = []
    for _str1 in str_list:
        if (len(_str1) >= 2) and (_str1[0] == _str1[len(_str1) - 1]):
            count += 1
            answer.append(_str1)
    return [count, answer]


def generate_string_form_first_and_last_char(input_str):
    if len(input_str) < 2:
        return ""
    answer = input_str[:2] + input_str[len(input_str) - 2:]
    return answer


def generate_list_of_squares(start, end):
    return [num * num for num in range(start, end)]


def sort_list_by_tuple_last_element(input_list):
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
    return [item for sublist in answer for item in sublist]


def modify_string(input_str):
    if len(input_str) < 3:
        return input_str
    if input_str.endswith("ing"):
        return input_str[:-3] + "ly"
    else:
        return input_str + "ing"


def find_min_max_of_list(number_list):
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
    return {element for element in list1 if element in list2}


def get_set_of_list(str_list):
    return {word for word in str_list if str_list.count(word) > 1}


def create_dict_comp(_list):
    return {len(val): val for val in _list}


def perform_set_operations(list_1, list_2):
    answer = {}
    answer["Union"] = list_1 | list_2
    answer["Intersection"] = list_1 & list_2
    answer["Difference"] = list_1 - list_2
    return answer


def get_set_of_merged_tuple(tuple_1, tuple_2):
    resultant_tuple = tuple_1 + tuple_2
    return set(resultant_tuple) # todo try using


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


str_list = ["abc", "xyz", "aba", "1221", "ww", "1222e31", "1234567"]
word_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
input_str = "Mo"
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
print(get_number_of_strings_with_condition(str_list)) #
print(generate_string_form_first_and_last_char(input_str))
print(generate_list_of_squares(1, 21))
print(sort_list_by_tuple_last_element(input_list))
print(modify_string(input_str))
min, max = find_min_max_of_list(number_list)
print("Minimum in list", min, " Maximum in list", max)
print(get_set_of_two_lists(list1, list2))
print(get_set_of_list(word_list))
print(perform_set_operations(set_1, set_2))
print(perform_set_operations(set_2, set_1))
print(get_set_of_merged_tuple(tuple_1, tuple_2))
print("word_count", get_words_with_more_than_one_occurrence(word_list))
