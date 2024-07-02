import math
from timeit import default_timer as timer


def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


nn = [2000, 4000, 8000, 16000, 32000]


def time_f1():
    for n in nn:
        start = timer()
        f1(n)
        stop = timer()
        Tn = stop - start
        Fn = n
        print(n, Tn, Fn / Tn)


def time_f2():
    for n in nn:
        start = timer()
        f2(n)
        stop = timer()
        Tn = stop - start
        Fn = n * n
        print(n, Tn, Fn / Tn)


def time_f3():
    for n in nn:
        start = timer()
        f3(n)
        stop = timer()
        Tn = stop - start
        Fn = n * n
        print(n, Tn, Fn / Tn)


def time_f4():
    for n in nn:
        start = timer()
        f4(n)
        stop = timer()
        Tn = stop - start
        Fn = n * math.log(n, 2)
        print(n, Tn, Fn / Tn)


def time_f5():
    for n in nn:
        start = timer()
        f5(n)
        stop = timer()
        Tn = stop - start
        Fn = math.log(n, 2)
        print(n, Tn, Fn / Tn)


# other time functions:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n

time_f1()
print("")
time_f2()
print("")
time_f3()
print("")
time_f4()
print("")
time_f5()

# result f1
# 2000 9.22000003811263e-05 21691973.87996332
# 4000 0.0001868999997896026 21401819.17872064
# 8000 0.000366799999937939 21810250.821574606
# 16000 0.0007353000000875909 21759825.91880054
# 32000 0.0014624000000367232 21881838.07384876

# result f2
# 2000 0.187677899999926 21313111.453194954
# 4000 0.7591349999997874 21076620.100515034
# 8000 3.049759600000016 20985260.608737707
# 16000 12.161562700000104 21049926.42105096
# 32000 47.76317240000026 21439111.94642495

# result f3
# 2000 0.09294080000017857 43038149.01520446
# 4000 0.3738832999997612 42794101.79596205
# 8000 1.4938897999995788 42841178.78040137
# 16000 5.954398800000035 42993425.29761333
# 32000 23.63510589999987 43325382.34999005

# result f4
# 2000 0.0013164999995751714 16658996.260084614
# 4000 0.002861899999970774 16724252.118919997
# 8000 0.006244500000320841 16610821.406352354
# 16000 0.013662500000009459 16355172.812767701
# 32000 0.02913269999999102 16438747.425035594

# result f5
# 2000 2.100000074278796e-06 5221801.855615682
# 4000 1.100000190490391e-06 10877983.829555176
# 8000 1.100000190490391e-06 11787074.581216037
# 16000 1.100000190490391e-06 12696165.332876898
# 32000 1.2000000424450263e-06 12471486.46275793
