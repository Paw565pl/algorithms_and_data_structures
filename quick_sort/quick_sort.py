from copy import deepcopy
from random import randint
from sys import setrecursionlimit
from timeit import default_timer as timer


def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        helper = A[j]
        i = j - 1
        while i >= 0 and A[i] > helper:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = helper


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    if i < r:
        return i
    else:
        return i - 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q)
        quick_sort(A, q + 1, r)
    return A


def better_quick_sort(A, c):
    def quick_sort(A, p, r, c):
        if p < r and c < r - p + 1:
            q = partition(A, p, r)
            quick_sort(A, p, q, c)
            quick_sort(A, q + 1, r, c)
        return A

    almost_sorted = quick_sort(A, 0, len(A) - 1, c)
    insertion_sort(almost_sorted)

    return A


def random_data():
    print("Random data test.")
    for n in nn:
        arr1 = [randint(1, n) for _ in range(n)]
        arr2 = deepcopy(arr1)

        start1 = timer()
        quick_sort(arr1, 0, len(arr1) - 1)
        stop1 = timer()

        time1 = stop1 - start1

        start2 = timer()
        better_quick_sort(arr2, 10)
        stop2 = timer()

        time2 = stop2 - start2

        print("quick_sort", n, time1, "|", "better_quick_sort", n, time2)


def unfavorable_data():
    print("Unfavorable data test.")
    for n in nn:
        arr1 = [x for x in range(n)]
        arr2 = deepcopy(arr1)

        start1 = timer()
        quick_sort(arr1, 0, len(arr1) - 1)
        stop1 = timer()

        time1 = stop1 - start1

        start2 = timer()
        better_quick_sort(arr2, 10)
        stop2 = timer()

        time2 = stop2 - start2

        print("quick_sort", n, time1, "|", "better_quick_sort", n, time2)


setrecursionlimit(1000000000)

nn = [1000, 5000, 10000, 15000]

random_data()
print("")
unfavorable_data()

# Random data
# quick_sort 1000 0.001679699998931028  |  better_quick_sort 1000 0.0013226000010035932
# quick_sort 5000 0.009902100006002001  |  better_quick_sort 5000 0.00807110000459943
# quick_sort 10000 0.023759999996400438  |  better_quick_sort 10000 0.020386599993798882
# quick_sort 15000 0.03172189999895636  |  better_quick_sort 15000 0.02650740000535734

# Unfavorable data
# quick_sort 1000 0.039884099998744205  |  better_quick_sort 1000 0.039559700002428144
# quick_sort 5000 1.0339317000034498  |  better_quick_sort 5000 1.0304617000074359
# quick_sort 10000 4.12447599999723  |  better_quick_sort 10000 4.180870000011055
# quick_sort 15000 9.263683299999684  |  better_quick_sort 15000 9.429881999996724
