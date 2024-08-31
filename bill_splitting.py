def bonApetit(bill, k, b):
    total = 0
    for i in range(len(bill)):
        if i != k:
            total += bill[i]
    total = total // 2
    if total == b:
        return "Bon Appetit"
    else:
        return b - total


if __name__ == "__main__":
    bill, k, b = [3, 10, 2, 9], 1, 12

    result = bonApetit(bill, k, b)
    print(result)
