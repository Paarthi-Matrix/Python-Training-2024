# 1st
a = input("Enter the word to calculate the character count:")


def calculate_count(i, a):
    print(i, a)
    c = 0
    for j in a:
        if j is i:
            c += 1
    return c

sample_dict = {i: calculate_count(i, a) for i in a}
print(sample_dict)

# 2nd
sample_l = ["zyx", "aba", "122341", "121", 121]


def count_the_strings(a):
    s = 0
    if a is None:
        return "Given Value is None"
    if len(a) == 0:
        return "Given list is Empty"
    for i in a:
        if isinstance(i, str) and len(i) >= 2 and i[0] == i[-1]:
            s += 1
    return s


print(count_the_strings(sample_l))

# 3rd
a3 = input("Enter the word to get and first two and last two characters:")


def get_first_and_last_two(a3):
    if isinstance(a3, str) and len(a3) > 2:
        return a3[:2] + a3[-2:]
    else:
        return "Given Input is Wrong"


print(get_first_and_last_two(a3))

# 4th
lq4 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (6, 2)]
lq41 = []
lq42 = []
for i in lq4:
    if i[1] not in lq41:
        lq41.append(i[1])
lq41.sort()

for k in lq41:
    for j in lq4:
        if k is j[1]:
            lq42.append(j)
print(lq42)

# 5th

a5 = input("Enter the word:")


def add_ing_or_ly(a5):
    if isinstance(a5, str) and len(a5) < 3:
        return a5
    elif isinstance(a5, str) and len(a5) >= 3 and a5[-3:] == "ing":
        return a5 + "ly"
    else:
        return a5 + "ing"


print(add_ing_or_ly(a5))

# 6th

lc = [x ** 2 for x in range(1, 21)]
print(lc)

# 7th
l = list(map(int, input("Enter the list of integers:").split()))
min = l[0]
max = l[0]


def get_min_and_max(l, mini, maxi):
    for num in l:
        if not isinstance(num, int):
            return print("given input is not an integer")
        elif num < mini:
            mini = num
        elif num > maxi:
            maxi = num
    return print("Minimum : ", mini, "Maximum : ", maxi)


get_min_and_max(l, min, max)

# 8th
l1 = [1, 2, 4, 2, 45, 342, 234, 123, "sriram", "sriram"]
l2 = [1, 4, 6, 1, 2, "sriram"]
l4 = "sriram"


def get_common_elements(l1, l2):
    l3 = []
    for i in l1:
        if i in l2:
            if i not in l3:
                l3.append(i)
    return l3


print(get_common_elements(l1, l2))

# 9th
l9 = input("enter the words Separated by space :").split()

same_in_l9 = []
for w in l9:
    if w not in same_in_l9 and calculate_count(w, l9) > 1:
        same_in_l9.append(w)
print(same_in_l9)


# 10th
s = {1, 3, 31, 132}
s1 = {31, 3, 14, 2, 1}


def get_intersection(s, s1):
    intersected_set = set()
    for i in s:
        if i in s1:
            if i not in intersected_set:
                intersected_set.add(i)
    return intersected_set


print(get_intersection(s, s1))


# 12th
def calculate_char_length(a1):
    char_length = {i: len(i) for i in a1}
    print(char_length)


calculate_char_length(input("Enter the word:"))

# 13th
t = (1, 2, 3, 4, 56, 7324)

t1 = tuple(x * 2 for x in t)

print(t1)

