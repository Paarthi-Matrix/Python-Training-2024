import math


def get_generator_over_list(element_list):
    for index, element in enumerate(element_list):
        yield index, element


def get_square_root_over_list(number_list):
    for number in number_list:
        yield math.sqrt(number)


def cumulative_product_generator(number_list):
    cumulative_product = 1
    for number in number_list:
        cumulative_product *= number
        yield cumulative_product


def generate_combinations(list_1, list_2):
    for element_1 in list_1:
        for element_2 in list_2:
            yield element_1, element_2


def merge_list_generator(list_1, list_2):
    answer = list_1 + list_2
    answer.sort()
    for num in answer:
        yield num


def find_cumulative_sum_of_sequence(number_list, window_size):
    cumulative_sum = 0
    for index in range(0, window_size):
        cumulative_sum += number_list[index]
    return cumulative_sum


def cumulative_sum_with_sliding_window_generator(number_list, window_size):
    start = 0
    end = window_size -1
    cumulative_sum_of_window = find_cumulative_sum_of_sequence(number_list, window_size)
    yield cumulative_sum_of_window
    loop_range = (len(number_list) + 1) - window_size
    for r in range(0, loop_range):
        cumulative_sum_of_window -= number_list[start]
        start += 1
        end += 1
        if end > len(number_list) - 1:
            break
        cumulative_sum_of_window += number_list[end]
        yield cumulative_sum_of_window
