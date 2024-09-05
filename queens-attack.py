def queensAttack(n, k, r_q, c_q, obstacles):
    queensDirections = [
        [1, 0],
        [-1, 0],
        [1, 1],
        [-1, -1],
        [0, 1],
        [0, -1],
        [1, -1],
        [-1, 1],
    ]
    currentPlace = [r_q, c_q]
    count = 0
    for i, j in queensDirections:
        currentPlace = [r_q, c_q]
        for _ in range(n):
            if (
                currentPlace[0] + i > n
                or currentPlace[0] + i < 1
                or currentPlace[1] + j > n
                or currentPlace[1] + j < 1
            ):
                print("Breaked", currentPlace)
                break
            currentPlace[0] += i
            currentPlace[1] += j
            if currentPlace in obstacles:
                print("Breaked", currentPlace)
                break
            else:
                print("Continue", currentPlace)
                count += 1

    return count


n = 5
k = 3
r_q = 4
c_q = 3
obstacles = [[5, 5], [4, 2], [2, 3]]

print(queensAttack(n, k, r_q, c_q, obstacles))
