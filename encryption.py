import math


def encryption(s):
    s = s.replace(" ", "")
    floor = math.floor(math.sqrt(len(s)))
    if floor == math.sqrt(len(s)):
        top = floor
    else:
        top = floor + 1
    encrypted = ""
    for _ in range(top):
        if len(s) < top:
            encrypted += s
            break
        for i in range(top):
            encrypted += s[i]
            if i == top - 1:
                s = s[top:]
                encrypted += " "
    encrypted = encrypted
    encrypted = encrypted.split(" ")
    a = ""
    for i in range(top):
        for j in encrypted:
            if len(j) <= i:
                break
            if j[i] is None:
                break
            a += j[i]

        a += " "
    return a[:-1]


text = "chillout"
print(encryption(text))
