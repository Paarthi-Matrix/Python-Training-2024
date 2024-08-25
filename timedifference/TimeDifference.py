import time

from timedifference.TimeIterator import TimeIterator

values = list(range(100000))


def calculate_for_loop_time():
    start_time = time.time()
    count = 0
    for value in values:
        count += 1
        if value % 2 != 0:
            if 64 < value < 1000:
                print(chr(value))
    print(count)
    end_time = time.time()
    for_loop_time = end_time - start_time
    print(f"For loop time: {for_loop_time} seconds")


def calculate_while_loop_time():
    start_time = time.time()
    index = 0
    while index < len(values):
        value = values[index]
        print(value)
        index += 1
    end_time = time.time()
    while_loop_time = end_time - start_time
    print(f"While loop time: {while_loop_time} seconds")


def calculate_list_comprehension_time():
    start_time = time.time()
    lst = [value for value in values]
    # print(lst)
    end_time = time.time()
    list_comprehension_time = end_time - start_time
    print(f"List comprehension time: {list_comprehension_time} seconds")


def calculate_map_lambda_time():
    start_time = time.time()
    print(list(map(lambda x: x**24, values)))
    end_time = time.time()
    map_lambda_time = end_time - start_time
    print(f"Map and lambda time: {map_lambda_time} seconds")


def calculate_iterator_time():
    start_time = time.time()
    iterator = TimeIterator(values)
    for i in iterator:
        if i % 2 == 0:
            print(i)
    end_time = time.time()
    print(iterator.__sizeof__())
    iterator_time = end_time - start_time
    print(f"Iterator time: {iterator_time} seconds")


def generator_time(val):
    count = 0
    while True:
        yield val[count]
        count += 1


def calculate_generator_time():
    start_time = time.time()
    generator = generator_time(values)
    for _ in range(len(values)):
        print(next(generator))
        pass
    end_time = time.time()
    cal_generator_time = start_time - end_time
    print(f"Generator time: {cal_generator_time} seconds")


if __name__ == "__main__":
    calculate_for_loop_time()
    calculate_while_loop_time()
    calculate_list_comprehension_time()
    calculate_map_lambda_time()
    calculate_iterator_time()
