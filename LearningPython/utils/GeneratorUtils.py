import math


def get_generator_over_list(element_list):
    for index, element in enumerate(element_list):
        yield index, element


def get_square_root_over_list(number_list):
    for number in number_list:
        yield math.sqrt(number)


def generate_combinations(list_1, list_2):
    for element_1 in list_1:
        for element_2 in list_2:
            yield element_1, element_2