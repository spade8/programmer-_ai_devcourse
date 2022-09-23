def solution(L, x):
    answer = []

    while x in L:
        index_x = L.index(x)
        if answer:
            answer.append(index_x + answer[-1] + 1)
        else:
            answer.append(index_x)
        L = L[index_x + 1:]

    if not answer:
        answer.append(-1)
    return answer