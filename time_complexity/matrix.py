from random import randint
from timeit import default_timer as timer


def max_rectangle_v1(n, M):
    max_area = 0
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(n - 1, x1 - 1, -1):
                for y2 in range(n - 1, y1 - 1, -1):
                    local_max = 0
                    for x in range(x1, x2 + 1):
                        for y in range(y1, y2 + 1):
                            local_max += M[x][y]
                    if (
                        local_max == (x2 - x1 + 1) * (y2 - y1 + 1)
                        and local_max > max_area
                    ):
                        max_area = local_max

    return max_area


def max_rectangle_v2(matrix):
    histograms = []
    histogram = [0] * len(matrix)

    for row in range(len(matrix)):
        for item in range(len(matrix)):
            if matrix[row][item] != 0:
                histogram[item] += 1
            else:
                histogram[item] = 0

        histograms.append(histogram.copy())

    max_area = 0

    for row in range(len(histograms)):
        for item in range(len(histograms)):
            bar_value = histograms[row][item]
            count = 1

            # if bar_value == 0:
            #     break

            for left in reversed(histograms[row][:item]):
                if left < bar_value:
                    break
                else:
                    count += 1
            for right in histograms[row][item + 1 :]:
                if right < bar_value:
                    break
                else:
                    count += 1
            area = bar_value * count
            if area > max_area:
                max_area = area

    return max_area


nn = [10, 20, 30, 40, 50]


def time_v1():
    for n in nn:
        m = [[randint(0, 1) for _ in range(n)] for _ in range(n)]
        start = timer()

        max_rectangle_v1(n, m)

        stop = timer()
        tn = stop - start
        fn = n ** 6  # time complexity
        print(n, tn, fn / tn)


def time_v2():
    for n in nn:
        m = [[randint(0, 1) for i in range(n)] for y in range(n)]
        start = timer()

        max_rectangle_v2(m)

        stop = timer()
        tn = stop - start
        fn = n ** 3  # time complexity
        print(n, tn, fn / tn)


print("function v1")
time_v1()

print("")

print("function v2")
time_v2()

# function v1
# 10 0.011060099815949798 90415097.20896891
# 20 0.23844750015996397 268402897.73247868
# 30 2.104396300157532 346417640.0354953
# 40 8.572474699933082 477808350.9575099
# 50 20.53394989995286 760934943.1614164

# function v2
# 10 0.00014560017734766006 6868123.502433845
# 20 0.0008634000550955534 9265693.177555602
# 30 0.001427799928933382 18910212.45544533
# 40 0.002425400074571371 26387399.205184903
# 50 0.0043669999577105045 28623769.455114443
