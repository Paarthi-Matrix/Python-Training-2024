import sys
import timeit
import time

from LearningPython.utils.CSVIterator import CSVIterator
from LearningPython.utils.SequenceIterator import SequenceIterator

#
# age = 10
#
# #float
# rate = 100.98
# print("rate hash value of rate before changing", hash(rate))
# rate = 22.09
# print("rate hash value of rate after changing", hash(rate))
#
# #String
# name = "Paarthiban"
# print("name hash value of rate before changing", hash(name))
# name = "Ranjith"
# print("name hash value of rate after changing", hash(name))
#
# #bool
# status = True
#
# #complex_number
# coordinates = 3 + 4j
#
# #list
# student_list = ["2A001", "Paarthiban K", 18]
# #tuple
# rgb = [256, 90, 53]
#
# #dict
# student_info = {"name": "Paarthiban K", "Age": 21, "marks": {"maths": 100, "Tamil": 90}}
#
# """dict properties"""
# print("get the keys from the dict")
# print(student_info.keys())
# print("it has the type of dict_keys")
# print(type(student_info.keys()))
#
# print("get the values from the dict")
# print(student_info.values())
# print("it has the type of dict_values")
# print(type(student_info.values()))
#
# #change the value by key
# student_info["name"] = "Arun"
# #remove the data by key
# print(student_info.pop("marks"))
# #get the elements by key
# print(student_info.get("name"))
# print(student_info)
#
number_list = [1, 2, 3, 4, 5, 6]
#
#
#
# for number in SequenceIterator(number_list):
#     print(number)

print("\n")


# number_list = SequenceIterator([1, 2, 3, 4, 5, 6, 7, 8, 9])
# iterator = iter(number_list)
# while True:
#     try:
#         item = iterator.__next__()
#     except StopIteration:
#         break
#     else:
#         print(item)


# # print(set(iter(number_list)))
# # d = {'foo': 1, 'bar': 2, 'baz': 3}
# # for k, v in d:
# #     print('k =', k, ', v =', v)
#
# Generators


def csv_reader(file_name):
    file = open(file_name)
    print(type(file))
    result = file.read().split("\n")
    return result


def csv_reader_using_generator(file_name):
    for row in open(file_name, "r"):
        yield row


def csv_reader_using_iterator(file_name):
    return CSVIterator(file_name)


def benchmark_csv_reader_using_iterator():
    for row in csv_reader_using_iterator("utils/data.csv"):
        pass


def benchmark_csv_reader():
    csv_reader("utils/data.csv")


def benchmark_csv_reader_using_generator():
    for row in csv_reader_using_generator("utils/data.csv"):
        pass


start_time = time.time()
csv_gen = (csv_reader("utils/data.csv"))
end_time = time.time()
print("Row count without using generator: ", len(csv_gen))
print("Type of   csv_gen", type(csv_gen))
print("Size of list", sys.getsizeof(csv_gen))
print("Time taken  for execution", end_time - start_time)
print()

csv_gen = (csv_reader_using_generator("utils/data.csv"))
print("Type of csv_gen", type(csv_gen))
print("Size of generation object", sys.getsizeof(csv_gen))
row_count = 0

start_time = time.time()
for row in csv_gen:
    row_count += 1
end_time = time.time()
print("Row count using generator: ", row_count)
print("Time taken for execution of generators", end_time - start_time)
print()

csv_itr = (csv_reader_using_iterator("utils/data.csv"))
print("Type of csv_gen", type(csv_itr))
print("Size of iterator object", sys.getsizeof(csv_itr))
row_count = 0

start_time = time.time()
for row in csv_itr:
    row_count += 1
end_time = time.time()
print("Row count using iterator: ", row_count)
print("Time taken for execution using iterator", end_time - start_time)
print()

csv_reader_time = timeit.timeit(benchmark_csv_reader, number=100)
csv_reader_generator_time = timeit.timeit(benchmark_csv_reader_using_generator, number=100)
csv_reader_iterator_time = timeit.timeit(benchmark_csv_reader_using_iterator, number=100)
print()
print("Bench mark results.")
print(f"csv_reader execution time (100 runs): {csv_reader_time} seconds")
print(f"csv_reader using generator execution time (100 runs): {csv_reader_generator_time} seconds")
print(f"csv_reader using iterator execution time (100 runs): {csv_reader_iterator_time} seconds")

# def generate_sequence(processed, un_processed, generated_sequence):
#     # Base case
#     if not un_processed:
#         generated_sequence.append(processed)
#         return generated_sequence
#
#     # accept
#     generate_sequence(processed + un_processed[0], un_processed[1:], generated_sequence)
#     # reject
#     return generate_sequence(processed, un_processed[1:], generated_sequence)
#
#
# sequence = "Paa"
# generated_sequence = []
#
# sequence_list = generate_sequence("", sequence, generated_sequence)
#
# print(sequence_list)


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# _generator = infinite_sequence()
#
# print(next(_generator))
# print(next(_generator))
# print(SequenceIterator)
