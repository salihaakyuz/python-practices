def countingValleys(steps, path):
    def returnMeaning(s):
        if s == "D":
            return -1
        if s == "U":
            return 1

    m = 0
    v = 0
    inValley = False

    for i in range(steps):
        m += returnMeaning(path[i])
        if m == -1 and not inValley:
            inValley = True
        if m == 0 and inValley:
            inValley = False
            v += 1
    return v


print(countingValleys(12, "DDUUDDUDUUUD"))
