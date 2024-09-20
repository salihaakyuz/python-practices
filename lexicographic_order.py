import math


def lexicographic_order(sets):
    order = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    new_set = ""
    for i in sets:
        previous = 0
        maximum = 0
        for j in range(len(i)):
            maximum = max(maximum, order[i[j]])
            if previous >= order[i[j]]:
                if j == len(i) - 1:
                    new_set += str(i) + "\n"
            elif i[len(i) - 1] > i[len(i) - 2]:
                new_text = i[: len(i) - 2] + i[len(i) - 1] + i[len(i) - 2]
                new_set += new_text + "\n"
                break
            previous = order[i[j]]

    return new_set[:-1]


sets = [
    "ac",
    "ab",
    "aa",
    "bc",
    "bd",
    "cd",
    "dc",
    "dd",
    "dcba",
    "dcbb",
    "dcbab",
    "fedcbabcd",
]
print(lexicographic_order(sets))
