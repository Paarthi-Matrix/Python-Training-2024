# 1
def get_no_character(str):
    dict = {}
    for e in str:
        if e in dict:
            continue
        else:
            dict[e] = find_count(e, str)
    return dict


# 2
def get_string(l1):
    l2 = []
    for e in l1:
        if (len(e) >= 2) and (e[0] == e[- 1]):
            l2.append(e)
    return l2


# 3
def generate_string(str):
    if len(str) >= 2:
        return str[0:2] + str[len(str) - 2:]


# 4
def find_sorted_tuple(ls):
    l1 = []
    for e in ls:
        if e[-1] not in l1:
            l1.append(e[-1])
    sort_list(l1)

    l2 = []
    for e1 in l1:
        for e2 in ls:
            if e1 == e2[-1]:
                l2.append(e2)
    return l2


# 5
def add_string(str):
    if len(str) >= 3:
        if str.endswith('ing'):
            str = str + 'ly'
        else:
            str = str + 'ing'
    return str


# 6
def generate_squares(start, end):
    return [n * n for n in range(start, end)]


# 7
def find_min_max(l1):
    min = l1[0]
    max = l1[0]
    for e in l1:
        if min > e:
            min = e
        if max < e:
            max = e
    return min, max


# 8
def get_common_elements(l1, l2):
    l3 = []
    for e in l1:
        if e not in l3 and e in l2:
            l3.append(e)
    return l3


# 9
def get_duplicate_words(l1):
    l2 = []
    for e in l1:
        if e not in l2 and find_count(e, l1) > 1:
            l2.append(e)
    return l2


# 10
def get_set(s1, s2):
    union_set = s1.union(s2)
    intersection_set = s1.intersection(s2)
    diff_set = s1.difference(s2)
    return "Union of s1,s2 " + str(union_set) + ", Intersection odf s1,s2 " + str(
        intersection_set) + ", difference of s1,s2 " + str(diff_set)


# 11
def calculate_mark(l1):
    dict = {}
    for i in range(len(l1)):
        e1 = l1[i][0]
        if e1 not in dict:
            val = l1[i][1]
            for i2 in range(i + 1, len(l1)):
                if e1 == l1[i2][0]:
                    val = l1[i2][1] + val
            dict[e1] = val

    return dict


# 12
def generate_dict(l1):
    return {len(e): [word for word in l1 if len(word) == len(e)] for e in l1}


# 13
def double_tuple(t1):
    l1 = []
    for e in t1:
        l1.append(e * e)
    return tuple(l1)


# 14
def swap_tuple(t1):
    a, e = t1[0], t1[-1]
    return (e,) + t1[1:-1] + (a,)


# 15
def get_tuple(t1, t2):
    l1 = []
    for e1 in t1:
        for e2 in t2:
            if e1 == e2:
                break
        else:
            l1.append(e1)
    return t2 + tuple(l1)


def find_count(val, l1):
    count = 0
    for e in l1:
        if e == val:
            count += 1
    return count


def sort_list(l1):
    for i1 in range(len(l1)):
        for i2 in range(i1 + 1, len(l1)):
            if l1[i1] > l1[i2]:
                temp = l1[i1]
                l1[i1] = l1[i2]
                l1[i2] = temp
    return l1


# 1
print(get_no_character('google.com'))
# 2
print(get_string(['abca', "xyc", 'abe', '1221']))
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
print('min:', min, 'max:',max)
# 8
print(get_common_elements([3, 8, 9, 4, 2], [5, 8, 9, 4, 1, 2]))
# 9
print(get_duplicate_words(['hari', 'ram', 'hari', 'janu','deepak', 'ram', 'deepak','deepak']))
# 10
print(get_set({'baz', 'quz', 'hari', 'john'}, {'ram', 'quz', 'john'}))
# 11
print(calculate_mark([('Alice', 90), ('Bob', 85), ('Alice', 95), ('Bob', 15), ('Alice', 15), ('Ram', 77)]))
# 12
print(generate_dict(['paa', 'abcd', 'xyzz', 'yrcs']))
# 13
print(double_tuple((2, 6, 5, 9)))
# 14
print(swap_tuple((5, 6, 8, 10, 12)))
# 15
print(get_tuple((7, 8, 9, 5.7, 10), (8, 10, 6, 5, 5.7)))
