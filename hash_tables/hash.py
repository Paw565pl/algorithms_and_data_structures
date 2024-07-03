def strong_hash(arg):
    output = 0
    for i in arg:
        output += 137 * ord(i)
    return output


def weak_hash(arg):
    return ord(arg[0])


def my_hash(func, list):
    return func % len(list)


def count_empty_lists(list):
    count = 0
    for i in list:
        if not i:
            count += 1
    return count


def longest(list):
    maximum = 0
    for i in list:
        if len(i) > maximum:
            maximum = len(i)
    return maximum


def avg_len_nonempty_lists(list):
    non_empty_lists = [len(el) for el in list if el != []]
    return round(sum(non_empty_lists) / len(non_empty_lists), 3)


with open("3700.txt", "r") as file:
    data = file.read().split("\n")


def compare_hash_functions(length: int, hash_func) -> list[list]:
    data_subset = [[] for _ in range(length)]

    for i in range(2 * length):
        data_subset[my_hash(hash_func(data[i]), data_subset)].append(data[i])

    print(f"{hash_func.__name__} for length {length}.")
    print("Number of empty lists:", count_empty_lists(data_subset))
    print("Max list length:", longest(data_subset))
    print("Average nonempty list length:", avg_len_nonempty_lists(data_subset))

    return data_subset


compare_hash_functions(17, hash)
print("")
compare_hash_functions(17, strong_hash)
print("")
compare_hash_functions(17, weak_hash)

print("---------------------------------------")
compare_hash_functions(1031, hash)
print("")
compare_hash_functions(1031, strong_hash)
print("")
compare_hash_functions(1031, weak_hash)
print("---------------------------------------")

compare_hash_functions(1024, hash)
print("")
compare_hash_functions(1024, strong_hash)
print("")
compare_hash_functions(1024, weak_hash)

# hash for length 17.
# Number of empty lists: 3
# Max list length: 5
# Average nonempty list length: 2.429
#
# strong_hash for length 17.
# Number of empty lists: 1
# Max list length: 4
# Average nonempty list length: 2.125
#
# weak_hash for length 17.
# Number of empty lists: 2
# Max list length: 5
# Average nonempty list length: 2.267
# ---------------------------------------
# hash for length 1031.
# Number of empty lists: 138
# Max list length: 7
# Average nonempty list length: 2.309
#
# strong_hash for length 1031.
# Number of empty lists: 325
# Max list length: 13
# Average nonempty list length: 2.921
#
# weak_hash for length 1031.
# Number of empty lists: 981
# Max list length: 183
# Average nonempty list length: 41.24
# ---------------------------------------
# hash for length 1024.
# Number of empty lists: 128
# Max list length: 9
# Average nonempty list length: 2.286
#
# strong_hash for length 1024.
# Number of empty lists: 325
# Max list length: 13
# Average nonempty list length: 2.93
#
# weak_hash for length 1024.
# Number of empty lists: 974
# Max list length: 183
# Average nonempty list length: 40.96

# best results give length: 1031
