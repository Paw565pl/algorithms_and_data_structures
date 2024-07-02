def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = " \\"
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = " |"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = " -"
    return c, b


def print_lcs_table(x, y):
    tables = lcs(x, y)
    numbers = tables[0]
    signs = tables[1]
    result = [[" i/j", " 0 "], []]
    for letter in y:
        result[0].append(" " + letter + " ")
    for i in range(len(numbers[0]) + 1):
        if i == 0:
            result[1].append("  0 ")
        else:
            result[1].append(" 0 ")
    for letter in x:
        result.append(["  " + letter + " ", " 0 "])
    for i in range(1, len(numbers)):
        for j in range(1, len(numbers[0])):
            result[i + 1].append(str(numbers[i][j]) + signs[i][j])
    result = "\n"
    for i in range(len(result)):
        for j in range(len(result[0])):
            result += result[i][j]
            if j != len(result[0]) - 1:
                result += " │ "
        result += "\n"
        if i != len(result) - 1:
            result += "_____" + "______" * (len(y) + 1) + "\n"
    print(result)


def lcs_results(x, y):
    def _lcs_results(x, c, b, i, j):
        result = set()
        if i == 0 or j == 0:
            result.add("")
            return result
        if b[i][j] == " \\":
            temp = _lcs_results(x, c, b, i - 1, j - 1)
            for element in temp:
                result.add(element + x[i - 1])
        else:
            if c[i - 1][j] >= c[i][j - 1]:
                result = _lcs_results(x, c, b, i - 1, j)
            if c[i][j - 1] >= c[i - 1][j]:
                temp = _lcs_results(x, c, b, i, j - 1)
                for element in temp:
                    result.add(element)
        return result

    data = lcs(x, y)
    elements = _lcs_results(x, data[0], data[1], len(x), len(y))

    return list(elements)


word_y = "labrador"
word_x = "abrakadabra"
lcs_list = lcs_results(word_y, word_x)
print_lcs_table(word_y, word_x)
print(lcs_list)
