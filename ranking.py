import bisect


# a = [1, 3, 4, 4, 4, 6, 7]
# print(bisect.bisect_left(a, 4))
# print(bisect.bisect_right(a, 4))
# def leaderboard(ranked, player):
#     ranked = sorted(list(set(ranked)))
#     # print(ranked)
#     aa = [bisect.bisect_right(ranked, score) for score in player]
#     print(aa)
#     for score in aa:
#         v = len(ranked) + 1 -score
#         print(v)
#     # return res
#
#
#def climbingLeaderboard(ranked, player):
    # return [sorted(set(ranked + [i]), reverse=True).index(i) + 1 for i in player]
#
#
#
#
#
# ranked = [100, 90, 90, 80]
# player = [70, 80, 105]
# print(leaderboard(ranked, player))

# def get_rank(leaderboard, score):
#     bisect.insort_right(leaderboard, score)
#     position = bisect.bisect_right(leaderboard, score)
#     rank = len(leaderboard) - position + 1
#     return rank
#
#
#
#
#
# leaderboard = [100, 90, 90, 80]
# new_score = [70, 80, 105]
# for score in new_score:
#     rank = get_rank(leaderboard, score)
#     print(f'Score: {score}, Rank: {rank}')
# # bisect.insort_right(a, b)
#
#
# def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
#     # Write your code here
#     ranked = [float("inf")] + ranked
#     el_ranked_dict = {ranked[0]: 0}
#     for i in range(1, len(ranked)):
#         if ranked[i] == ranked[i - 1]:
#             el_ranked_dict[ranked[i]] = el_ranked_dict[ranked[i - 1]]
#         else:
#             el_ranked_dict[ranked[i]] = el_ranked_dict[ranked[i - 1]] + 1
#     last_index = len(ranked)
#     result = []
#     for score in player:
#         for i in range(last_index, 0, -1):
#             el = ranked[i - 1]
#             if el > score:
#                 last_index = i
#                 result.append(el_ranked_dict[el] + 1)
#                 break
#     return result
#
#
# def climbingLeaderboard(ranked, player):
#     # Max rank is number of unique values in ranked list plus one
#     rank = len(set(ranked))+1
#     ranked_index = len(ranked) - 1
#     results = []
#     for score in player:
#         while score >= ranked[ranked_index]:
#             if ranked_index == 0:
#                 rank = 1
#                 break
#             rank = rank if ranked[ranked_index] == ranked[ranked_index-1] else rank - 1
#             ranked_index -= 1
#         results.append(rank)
#     return results
#
#
# def climbingLeaderboard(ranked, player):
#     # Step 1: Remove duplicates from the ranked list and sort in descending order
#     unique_scores = list(set(ranked))
#     unique_scores.sort(reverse=True)
#
#     result = []
#     num_unique_scores = len(unique_scores)
#
#     # Step 2: For each score in the player's list, determine the rank
#     for player_score in player:
#         # Step 3: Adjust the rank based on the current player score
#         while num_unique_scores > 0 and player_score >= unique_scores[num_unique_scores - 1]:
#             num_unique_scores -= 1
#         # Append the rank to the result list
#         result.append(num_unique_scores + 1)
#
#     return result
#
#
# ranked = sorted(set(ranked), reverse=True)
# results = []
# l = len(ranked)
#
# for score in player:
#     print(l)
#     while (l > 0) and (score >= ranked[l - 1]):
#         l -= 1
#
#     results.append(l + 1)
#
# return results

def ranking_from_player(ranked, player):
    ranking = []
    for score in player:
        ranked.append(score)
        temp_score = sorted(ranked, reverse=True)
        print(temp_score)
        ranks = {}
        curr = 1
        ranks[temp_score[0]] = curr
        for i in range(1, len(temp_score)):
            if temp_score[i] != temp_score[i-1]:
                curr += 1
            ranks[temp_score[i]] = curr
        ranking.append((ranks[score]))
    return ranking

print(ranking_from_player([100, 90, 90, 80], [70, 80, 105]))


import bisect

def calculate_dense_ranks(leaderboard, players):

    leaderboard = sorted(set(leaderboard))

    score_rank = []

    for score in players:
        bisect.insort_right(leaderboard, score)
        position = bisect.bisect_right(leaderboard, score)
        
        rank = len(leaderboard) - position + 1

        score_rank.append(rank)

    return score_rank

print(calculate_dense_ranks([100, 90, 90, 80], [70, 80, 105]))
print()


def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked))
    return [len(ranked) - bisect.bisect_right(ranked, i)+1 for i in player]

print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))