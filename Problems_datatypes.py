# 1.Write a Python program to count the number of characters in a string.

def character_count():
    input_string = input("Enter the string : ")
    count_dictionary = dict()
    for character in input_string:
        count_dictionary[character] = input_string.count(character)
    return count_dictionary


if __name__ == '__main__':
    print(character_count())

# 2. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.


def string_case_match(input_list):
    string_count = 0
    match_list = list()
    for word in input_list:
        if (len(word) >= 2) and (word[0] == word[-1]):
            match_list.append(word)
            string_count += 1
    return f'The no. of strings matching conditions are {match_list} and of count {string_count}'


if __name__ == '__main__':
    words_list = ["ww", "abinaava", "arathia", "malayalam"]
    print(string_case_match(words_list))


# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead the empty string

def make_string():
    input_string = input("Please enter the string : ")
    if len(input_string) < 2:
        return ''
    elif len(input_string) >= 2:
        return input_string[:2]+input_string[-2:]
    else:
        return ''


if __name__ == '__main__':
    print(make_string())

# 4 .Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# from a given list of non-empty tuples. Go to the editor
#  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def last(n):
    return n[-1]


def arrange_sort(input_value):
    return sorted(input_value, key=last)


if __name__ == '__main__':
    tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(arrange_sort(tuple_list))


def bubble_sort(input_value):
    input_length = len(input_value)
    for count in range(input_length):
        for each in range(input_length - count - 1):
            if input_value[each][-1] > input_value[each + 1][-1]:
                #if condition satisfied, swapping the last element with the last before
                input_value[each], input_value[each + 1] = input_value[each + 1], input_value[each]
    return input_value


if __name__ == '__main__':
    tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(bubble_sort(tuple_list))


# 5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string is already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged

def add_suffix():
    string_value = input("Please enter the string : ")
    if len(string_value) < 3:
        return string_value
    elif string_value.isalpha():
        if string_value.endswith('ing'):
            return string_value + 'ly'
        else:
            return string_value + 'ing'
    else:
        return "Please enter the string value in characters"


if __name__ == '__main__':
    print(add_suffix())


# 6. Create a list comprehension that generates a list of squares of numbers from 1 to 20.

list_of_squares = [i**2 for i in range(1,21)]
print(list_of_squares)

# 7. Given a list of integers, find the largest and smallest numbers in the list without using the
# built-in max() and min() functions.


def min_finder(num_list):
    min = num_list[0]
    for number in num_list:
        if min > number:
            min = number
    return 'The minimum value in the list is ', min


def max_finder(num_list):
    max = num_list[0]
    for number in num_list:
        if max < number:
            max = number
    return 'The maximum value in the list is ', max


if __name__ == '__main__':
    int_list = [10, 9, 3, 1, 13, 11, 24]
    print(min_finder(int_list))
    print(max_finder(int_list))

# 8. Write a function that takes two lists and returns a set of elements that are common to both lists.


def common_elements(list1, list2):
    common_element = list()
    for element in list1:
        if element in list2:
            common_element.append(element)
        else:
            continue
    return common_element


if __name__ == '__main__':
    name_list = ['abinaav', 'racikha', 'puppy', 'arjun', 'pappu']
    nick_list = ['arjun', 'racikha', 'pappu']
    print(common_elements(name_list, nick_list))


# 9. Given a list of words, return a set of words that appear more than once in the list.


def list_of_words(input_list):
    name_dict = dict()
    for names in input_list:
        if names in name_dict:
            name_dict[names] += 1
        else:
            name_dict[names] = 1
    print([name for name, count in name_dict.items() if name_dict[name] > 1])


if __name__ == '__main__':
    words_list = ['abinaav', 'rahul', 'kiwi', 'rekha', 'abinaav', 'rekha']
    list_of_words(words_list)

# 10. Given two sets, write a function to return their union, intersection, and difference.

def set_functions(set1, set2):
    print('Union :', set1.union(set2),
          '\nIntersection :', set1.intersection(set2),
          '\nDifference :', set1.difference(set2))


if __name__ == '__main__':
    set_a = {'python', 'java', 'web3', 'react', 'machine learning', 11, 22}
    set_b = {'python', 'node', 'web3', 'datascience', 11}
    set_functions(set_a, set_b)


# 15. Write a function that takes two tuples and returns a new tuple that contains all elements
# from both tuples without any duplicates.


def tuple_without_duplicates(names, values):
    combined = names + values
    seen = list()
    for value in combined:
        if value not in seen:
            seen.append(value)
    return tuple(seen)


if __name__ == '__main__':
    courses = ('Maths', 'Science', 'Social', 'EVS')
    subjects = ('Maths', 'English','Science', 'Social', 'History')
    print('The combination of two tuples without duplicates are : ', tuple_without_duplicates(courses, subjects))


# 11. Given a list of tuples where each tuple contains a name and a score
# write a function to return a dictionary where each name maps to the sum of their scores.
# (e.g., [('Alice', 90), ('Bob', 85), ('Alice', 95)])

def tuple_to_dict(input_list):
    marks_dict = dict()
    for each in input_list:
        if each[0] not in marks_dict:
            marks_dict[each[0]] = [each[1]]
        else:
            marks_dict[each[0]].append((each[1]))
    return marks_dict


if __name__ == '__main__':
    list_of_tuples = [('Alice', 90), ('Bob', 85), ('Alice', 95), ('Alice', 100), ('Bob', 95), ('alice', '56'), ('alice', '96'), ('abinaav', 90)]
    print(tuple_to_dict(list_of_tuples))
