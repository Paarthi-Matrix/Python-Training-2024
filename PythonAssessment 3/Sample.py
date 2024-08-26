# Positional and keyword Arguments
import sys


def name():
    age = 21
    return age


def age():
    name = "sriram"
    return name


def fun_check(name, age, salary="Nothing"):
    print("Hii I'm ", name)
    print("My Age is :", age)
    print("Salary :", salary)


# print(fun_check("sriram", 22))
# print(fun_check(22, "sriram"))
# print(fun_check(name="sriram", age=22))
# print(fun_check(age=22, name="sriram"))
# print(fun_check(name(), age()))
# print(fun_check(salary=20000,"sriram", 22))
# print(fun_check("sriram", name="sr", salary=20000))
# print(fun_check(name="sriram","sriram",salary=12)) #keyword followed by positional
print(fun_check("sriram", age=22, salary=20000))  # positional followed by keyword

# Passing dictionary as keyword arguments Using ** ( splat ) operator
# test_dict = {"a":"Sriram","b":21}
# print("The function values with splat operator unpacking : ")
# print(fun_check(**test_dict))
# test_dict = {"age": 21, "name": "Sriram"}
# print("The function values with splat operator unpacking : ")
# print(fun_check(**test_dict))
#
# l1 = [1, 2, 3, 4, 5, 6, 7, 8,"sriram"]
# l = map(lambda a: a * 2, l1)
# print(list(l))
#
# lst = ["sriram"]
# print(sys.getsizeof(lst))
# print(lst.__sizeof__())
