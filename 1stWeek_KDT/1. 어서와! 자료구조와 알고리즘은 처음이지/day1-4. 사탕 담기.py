from itertools import combinations
def solution(m, weights):
    answer = 0
    for i in range(1, len(weights) + 1):
        combi = list(combinations(weights, i))
        for j in combi:
            if sum(j) == m:
                answer += 1

    return answer