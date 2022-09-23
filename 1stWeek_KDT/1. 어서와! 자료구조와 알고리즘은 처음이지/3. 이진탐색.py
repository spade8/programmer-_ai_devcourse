def solution(L, x):
    idx = -1
    lower = 0
    upper = len(L) -1
    while lower <= upper:
        middle = (upper + lower) // 2
        if L[middle] == x:
            idx = middle
            break
        elif L[middle] > x:
            upper = middle-1
        else:
            lower = middle +1
    return idx