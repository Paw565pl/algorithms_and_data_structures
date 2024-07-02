def insert(data, size, procent, method):
    output_list = [[]] * size
    number_of_tries = 0
    for i in range(int(size * procent / 100)):
        success = False
        hash_result = 0
        j = 0
        for letter in data[i]["surname"]:
            hash_result = hash_result * 331 + ord(letter)
        while not success:
            number_of_tries += 1
            index = method(hash_result, j, size)
            if not output_list[index]:
                output_list[index] = data[i]
                success = True
            else:
                j += 1
                if j == size:
                    break

    output = f"{output_list}\nAverage number of attempts for {method.__name__}: {round(number_of_tries / (size * procent / 100), 4)} at {procent}% full."

    return output


def linear_hash(hash_result, j, m):
    return (hash_result + j) % m


def quadratic_hash(hash_result, j, m):
    return (hash_result + j * j) % m


def double_hash(hash_result, j, m):
    return (hash_result + j * (1 + (hash_result % (m - 2)))) % m


def print_hash_results(data, size):
    print(f"------------ SIZE: {size} ------------")
    for percentage in [50, 70, 90]:
        for hash_method in [linear_hash, quadratic_hash, double_hash]:
            print(insert(data, size, percentage, hash_method))
        print("")


with open("surnames", "r") as f:
    surnames = [{"amount": line.split()[0], "surname": line.split()[1]} for line in f]

print_hash_results(surnames, 19)
# print_hash_results(surnames, 5503)
# print_hash_results(surnames, 18869)

# ------------ SIZE: 19 ------------
# [{'amount': '131940', 'surname': 'Kowalski'}, {'amount': '92945', 'surname': 'Dabrowski'}, [], [], [], {'amount': '89366', 'surname': 'Lewandowski'}, [], [], [], {'amount': '87935', 'surname': 'Kaminski'}, [], [], {'amount': '220217', 'surname': 'Nowak'}, [], {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, [], {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for linear_hash: 1.0526 at 50% full.
# [{'amount': '131940', 'surname': 'Kowalski'}, {'amount': '92945', 'surname': 'Dabrowski'}, [], [], [], {'amount': '89366', 'surname': 'Lewandowski'}, [], [], [], {'amount': '87935', 'surname': 'Kaminski'}, [], [], {'amount': '220217', 'surname': 'Nowak'}, [], {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, [], {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for quadratic_hash: 1.0526 at 50% full.
# [{'amount': '131940', 'surname': 'Kowalski'}, [], [], [], [], {'amount': '89366', 'surname': 'Lewandowski'}, [], [], [], {'amount': '87935', 'surname': 'Kaminski'}, [], [], {'amount': '220217', 'surname': 'Nowak'}, [], {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, {'amount': '92945', 'surname': 'Dabrowski'}, {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for double_hash: 1.0526 at 50% full.

# [{'amount': '131940', 'surname': 'Kowalski'}, {'amount': '92945', 'surname': 'Dabrowski'}, {'amount': '72368', 'surname': 'Kozlowski'}, [], [], {'amount': '89366', 'surname': 'Lewandowski'}, [], [], {'amount': '65942', 'surname': 'Jankowski'}, {'amount': '87935', 'surname': 'Kaminski'}, {'amount': '84527', 'surname': 'Szymanski'}, [], {'amount': '220217', 'surname': 'Nowak'}, {'amount': '81390', 'surname': 'Wozniak'}, {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, [], {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for linear_hash: 1.3534 at 70% full.
# [{'amount': '131940', 'surname': 'Kowalski'}, {'amount': '92945', 'surname': 'Dabrowski'}, [], {'amount': '72368', 'surname': 'Kozlowski'}, [], {'amount': '89366', 'surname': 'Lewandowski'}, [], [], {'amount': '65942', 'surname': 'Jankowski'}, {'amount': '87935', 'surname': 'Kaminski'}, {'amount': '84527', 'surname': 'Szymanski'}, [], {'amount': '220217', 'surname': 'Nowak'}, {'amount': '81390', 'surname': 'Wozniak'}, {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, [], {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for quadratic_hash: 1.2782 at 70% full.
# [{'amount': '131940', 'surname': 'Kowalski'}, [], [], {'amount': '72368', 'surname': 'Kozlowski'}, [], {'amount': '89366', 'surname': 'Lewandowski'}, {'amount': '84527', 'surname': 'Szymanski'}, [], {'amount': '65942', 'surname': 'Jankowski'}, {'amount': '87935', 'surname': 'Kaminski'}, [], [], {'amount': '220217', 'surname': 'Nowak'}, {'amount': '81390', 'surname': 'Wozniak'}, {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, {'amount': '92945', 'surname': 'Dabrowski'}, {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for double_hash: 1.2782 at 70% full.

# [{'amount': '131940', 'surname': 'Kowalski'}, {'amount': '92945', 'surname': 'Dabrowski'}, {'amount': '72368', 'surname': 'Kozlowski'}, {'amount': '59403', 'surname': 'Kaczmarek'}, {'amount': '59069', 'surname': 'Mazur'}, {'amount': '89366', 'surname': 'Lewandowski'}, {'amount': '62629', 'surname': 'Kwiatkowski'}, [], {'amount': '65942', 'surname': 'Jankowski'}, {'amount': '87935', 'surname': 'Kaminski'}, {'amount': '84527', 'surname': 'Szymanski'}, [], {'amount': '220217', 'surname': 'Nowak'}, {'amount': '81390', 'surname': 'Wozniak'}, {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, {'amount': '63519', 'surname': 'Wojciechowski'}, {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for linear_hash: 2.1637 at 90% full.
# [{'amount': '131940', 'surname': 'Kowalski'}, {'amount': '92945', 'surname': 'Dabrowski'}, {'amount': '59403', 'surname': 'Kaczmarek'}, {'amount': '72368', 'surname': 'Kozlowski'}, [], {'amount': '89366', 'surname': 'Lewandowski'}, {'amount': '62629', 'surname': 'Kwiatkowski'}, [], {'amount': '65942', 'surname': 'Jankowski'}, {'amount': '87935', 'surname': 'Kaminski'}, {'amount': '84527', 'surname': 'Szymanski'}, {'amount': '59069', 'surname': 'Mazur'}, {'amount': '220217', 'surname': 'Nowak'}, {'amount': '81390', 'surname': 'Wozniak'}, {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, {'amount': '63519', 'surname': 'Wojciechowski'}, {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for quadratic_hash: 1.6959 at 90% full.
# [{'amount': '131940', 'surname': 'Kowalski'}, {'amount': '59069', 'surname': 'Mazur'}, {'amount': '63519', 'surname': 'Wojciechowski'}, {'amount': '72368', 'surname': 'Kozlowski'}, [], {'amount': '89366', 'surname': 'Lewandowski'}, {'amount': '84527', 'surname': 'Szymanski'}, {'amount': '62629', 'surname': 'Kwiatkowski'}, {'amount': '65942', 'surname': 'Jankowski'}, {'amount': '87935', 'surname': 'Kaminski'}, [], {'amount': '59403', 'surname': 'Kaczmarek'}, {'amount': '220217', 'surname': 'Nowak'}, {'amount': '81390', 'surname': 'Wozniak'}, {'amount': '87690', 'surname': 'Kowalczyk'}, {'amount': '104418', 'surname': 'Wisniewski'}, {'amount': '85988', 'surname': 'Zielinski'}, {'amount': '92945', 'surname': 'Dabrowski'}, {'amount': '88932', 'surname': 'Wojcik'}]
# Average number of attempts for double_hash: 1.8129 at 90% full.
