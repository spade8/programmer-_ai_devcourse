def solution(L, x):
    answer = []
    index_x = 0

    for i in range(len(L)):
        print(i)
        if L[i] > x:
            index_x = i
            break
        elif i == len(L) - 1:
            index_x = i + 1

    L.insert(index_x, x)

    answer = L

    return answer