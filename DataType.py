# 1
def get_no_of_characters(s):
    """
    Counts the number of occurrences of each character in a given string.

    Args:
        s (str): The string to analyze.

    Returns:
        dict: A dictionary where the keys are characters and the values are
              the number of times each character appears in the string.
    """
    char_count = {}
    for char in s:
        if char in char_count:
            continue
        else:
            char_count[char] = find_count(char, s)
    return char_count


# 2
def get_strings_with_matching_ends(strings_list):
    """
    Returns a list of strings from the input list that have at least two characters
    and start and end with the same character.

    Args:
         strings_list(list): A list of strings to be checked.

    Returns:
        list: A list of strings which have at least two characters
              and start and end with the same character.
    """
    matching_strings = []
    for string in strings_list:
        if len(string) >= 2 and string[0] == string[-1]:
            matching_strings.append(string)
    return matching_strings


# 3
def generate_string(input_string):
    """
       Returns a new string composed of the first two and the last two characters
       of the input string. If the input string has fewer than two characters,
       it returns an empty string.

       Args:
           input_string (str): The string to process.

       Returns:
           str: A string composed of the first two and last two characters, or
                an empty string if the input is too short.
       """

    if len(input_string) >= 2:
        return input_string[0:2] + input_string[len(input_string) - 2:]
    return ''


# 4
def find_sorted_tuple(input_list):
    """
        Returns a list of tuples sorted by the last element of each tuple. The
        sorting is based on unique last elements of the tuples.

        Args:
            input_list (list): A list of tuples to be sorted.

        Returns:
            list: A list of tuples sorted by the last element.
        """
    last_elements = []
    for tup in input_list:
        if tup[-1] not in last_elements:
            last_elements.append(tup[-1])
    sort_list(last_elements)

    sorted_tuples = []
    for element in last_elements:
        for tup in input_list:
            if element == tup[-1]:
                sorted_tuples.append(tup)
    return sorted_tuples


# 5
def add_string(input_string):
    """

    Adds 'ing' to the end of the input string if it has at least 3 characters.
    If the string already ends with 'ing', 'ly' is added instead. If the string
    has fewer than 3 characters, it is returned unchanged.

    Args:
        input_string (str): The string to modify.

    Returns:
        str: The modified string with 'ing' or 'ly' appended, or the original
             string if it is too short.
    """
    if len(input_string) >= 3:
        if input_string.endswith('ing'):
            input_string = input_string + 'ly'
        else:
            input_string = input_string + 'ing'
    return input_string


# 6
def generate_squares(start, end):
    """

    Generates a list of squares of integers from the start value (inclusive)
    to the end value (exclusive).

    Args:
        start (int): The starting integer.
        end (int): The ending integer (exclusive).

    Returns:
        list: A list of squares of integers from start to end-1.
    """
    return [n * n for n in range(start, end)]


# 7
def find_min_max(values):
    """

    Finds the minimum and maximum values in a list of numbers.

    Args:
        values (list): A list of numbers.

    Returns:
        tuple: A tuple containing the minimum and maximum values from the list.
    """
    min_value = values[0]
    max_value = values[0]
    for value in values:
        if min_value > value:
            min_value = value
        if max_value < value:
            max_value = value
    return min_value, max_value


# 8
def get_common_elements(list1, list2):
    """

    Finds and returns a list of common elements between two lists.
    Duplicates within the same list are ignored, and elements are added to the
    result list only once.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        list: A list of unique elements that are present in both input lists.
    """
    common_elements = []
    for element in list1:
        if element not in common_elements and element in list2:
            common_elements.append(element)
    return common_elements


# 9
def get_duplicate_words(words_list):
    """
    Finds and returns a list of duplicate words from the input list.
    Words are included in the result list only once.

    Args:
        words_list (list): A list of words to check for duplicates.

    Returns:
        list: A list of words that appear more than once in the input list.
    """
    duplicates = []
    for e in words_list:
        if e not in duplicates and find_count(e, words_list) > 1:
            duplicates.append(e)
    return duplicates


# 10
def get_set(set1, set2):
    """
    Computes the union, intersection, and difference of two sets and returns
    a formatted string with the results.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        str: A string summarizing the union, intersection, and difference
             of the two sets.
    """
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    diff_set = set1.difference(set2)
    return "Union of s1,s2 " + str(union_set) + ", Intersection odf s1,s2 " + str(
        intersection_set) + ", difference of s1,s2 " + str(diff_set)


# 11
def calculate_marks(data_list):
    """
    Calculates the total marks for each unique student from the input list.
    Each entry in the list is a tuple where the first element is the student's name
    and the second element is the student's marks. The function sums up the marks
    for each student and returns a dictionary with students' names as keys and their
    total marks as values.

    Args:
        data_list (list of tuple): A list of tuples where each tuple contains
                                   a student's name and their marks.

    Returns:
        dict: A dictionary where the keys are students' names and the values are
              their total marks.
    """
    marks_dict = {}
    for i in range(len(data_list)):
        e1 = data_list[i][0]
        if e1 not in marks_dict:
            val = data_list[i][1]
            for i2 in range(i + 1, len(data_list)):
                if e1 == data_list[i2][0]:
                    val = data_list[i2][1] + val
            marks_dict[e1] = val

    return marks_dict


# 12
def generate_dict(words_list):
    """
    Generates a dictionary where the keys are word lengths and the values are lists
    of words from the input list that have the corresponding length.

    Args:
        words_list (list of str): A list of words.

    Returns:
        dict: A dictionary where the keys are word lengths and the values are lists
              of words that have those lengths.
    """

    return {len(e): [word for word in words_list if len(word) == len(e)] for e in words_list}


# 13
def double_tuple(t1):
    """
    Returns a tuple containing each element of the input tuple squared.

    Args:
        t1 (tuple): A tuple of numbers.

    Returns:
        tuple: A tuple where each element is the square of the corresponding
               element in the input tuple.
    """
    squared_elements = []
    for e in t1:
        squared_elements.append(e * e)
    return tuple(squared_elements)


# 14
def swap_tuple(t1):
    """
    Swaps the first and last elements of the input tuple.

    Args:
        t1 (tuple): A tuple with at least two elements.

    Returns:
        tuple: A tuple with the first and last elements swapped.
    """
    a, e = t1[0], t1[-1]
    return (e,) + t1[1:-1] + (a,)


# 15
def get_tuple(t1, t2):
    """
    Returns a new tuple consisting of the elements of the second tuple
    followed by the elements of the first tuple that are not present in the second tuple.

    Args:
        t1 (tuple): The first tuple from which unique elements are taken.
        t2 (tuple): The second tuple to which unique elements from the first tuple are appended.

    Returns:
        tuple: A tuple containing elements from the second tuple followed by unique elements
               from the first tuple not found in the second tuple.
    """
    lst = []
    for e1 in t1:
        for e2 in t2:
            if e1 == e2:
                break
        else:
            lst.append(e1)
    return t2 + tuple(lst)


def find_count(value, lst):
    """

    Counts the number of occurrences of a specified value in a list.

    Args:
        value: The value to count in the list.
        lst (list): The list in which to count occurrences of the value.

    Returns:
        int: The number of times the value appears in the list.
    """
    count = 0
    for e in lst:
        if e == value:
            count += 1
    return count


def sort_list(lst):
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Args:
        lst (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                # Swap elements
                lst[i], lst[j] = lst[j], lst[i]

    return lst


# 1
print(get_no_of_characters('google.com'))
# 2
print(get_strings_with_matching_ends(['abca', "xyc", 'abe', '1221']))
# 3
print(generate_string('run'))
# 4
print(find_sorted_tuple([(2, 5), (1, 2), (4, 4), (6, 2), (2, 3), (2, 1), (8, 2)]))
# 5
print(add_string('runing'))
# 6
print(generate_squares(1, 21))
# 7
min, max = find_min_max([50, 4, 8, 15, 20, 3])
print('min:', min, 'max:', max)
# 8
print(get_common_elements([3, 8, 9, 4, 2], [5, 8, 9, 4, 1, 2]))
# 9
print(get_duplicate_words(['hari', 'ram', 'hari', 'janu', 'deepak', 'ram', 'deepak', 'deepak']))
# 10
print(get_set({'baz', 'quz', 'hari', 'john'}, {'ram', 'quz', 'john'}))
# 11
print(calculate_marks([('Alice', 90), ('Bob', 85), ('Alice', 95), ('Bob', 15), ('Alice', 15), ('Ram', 77)]))
# 12
print(generate_dict(['paa', 'abcd', 'xyzz', 'yrcs']))
# 13
print(double_tuple((2, 6, 5, 9)))
# 14
print(swap_tuple((5, 6, 8, 10, 12)))
# 15
print(get_tuple((7, 8, 9, 5.7, 10), (8, 10, 6, 5, 5.7)))
