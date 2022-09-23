def solution(d, budget):
    sum_d = 0
    cnt = 0
    d.sort()

    for i in d:
        sum_d += i
        if sum_d > budget:
            break
        else:
            cnt += 1

    return cnt