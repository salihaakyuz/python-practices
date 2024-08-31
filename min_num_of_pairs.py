# find the minimum number of pairs that can be formed from the given array such that the sum of the pairs is divisible by k
def divisibleSumPairs(ar):
    x = {"types": [], "counts": []}

    for i in range(len(ar)):
        if ar[i] not in x["types"]:
            x["types"].append(ar[i])
            x["counts"].append(1)
        else:
            index = x["types"].index(ar[i])
            x["counts"][index] += 1
    max_count = max(x["counts"])
    maxs = []
    for i in range(len(x["types"])):
        if x["counts"][i] == max_count:
            maxs.append(x["types"][i])

    return min(maxs)


if __name__ == "__main__":
    ar = [10, 5, 20, 20, 10, 5, 4, 5, 10, 25, 25, 20]

    result = divisibleSumPairs(ar)
    print(result)
