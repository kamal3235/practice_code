


def breaking_recor(scores):
    most_point = scores[0]
    least_point = scores[0]
    count_least = 0
    count_most = 0
    for i in range(1, len(scores)):
        if most_point < scores[i]:
            most_point = scores[i]
            count_most += 1
            # print(i, most_point, scores[i], count_most )
        elif least_point > scores[i]:
            least_point = scores[i]
            count_least += 1
            print(i, least_point, scores[i], count_least)
    return [count_most, count_least]
# Initial values: most_point = 10, least_point = 10, count_most = 0, count_least = 0
# Iteration 1: scores[1] = 5 (new lowest), least_point = 5, count_least = 1
# Iteration 2: scores[2] = 20 (new highest), most_point = 20, count_most = 1
# Iteration 3: scores[3] = 20 (no change)
# Iteration 4: scores[4] = 4 (new lowest), least_point = 4, count_least = 2
# Iteration 5: scores[5] = 5 (no change)
# Iteration 6: scores[6] = 2 (new lowest), least_point = 2, count_least = 3
# Iteration 7: scores[7] = 25 (new highest), most_point = 25, count_most = 2
# Iteration 8: scores[8] = 1 (new lowest), least_point = 1, count_least = 4
# Final output: [2, 4]

print(breaking_recor([10, 5, 20, 20, 4, 5, 2, 25, 1]))