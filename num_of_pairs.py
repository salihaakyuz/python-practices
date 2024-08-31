def sockMerchant(n, ar):
    x = {"colors": [], "counts": []}
    ar.sort()
    for i in ar:
        if i not in x["colors"]:
            x["colors"].append(i)
    for i in range(len(x["colors"])):
        x["counts"].append(ar.count(x["colors"][i]))
    m = 0
    for i in x["counts"]:
        m += int(i / 2)
    return m


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
