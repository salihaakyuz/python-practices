def climbingLeaderboard(ranked, player):
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    scores = []
    for i in player:

        if i in ranked:
            scores.append(ranked.index(i) + 1)
        elif i < ranked[-1]:
            scores.append(len(ranked) + 1)
        elif i > ranked[0]:
            scores.append(1)
        else:
            for j in range(len(ranked) - 1):
                if ranked[j] >= i > ranked[j + 1]:
                    scores.append(j + 2)

    return scores


# Example big data case
ranked = [100, 90, 90, 80, 75, 60, 60, 50, 50, 45, 40, 30, 20, 10, 5]
player = [50, 65, 77, 90, 102]
print(climbingLeaderboard(ranked, player))
