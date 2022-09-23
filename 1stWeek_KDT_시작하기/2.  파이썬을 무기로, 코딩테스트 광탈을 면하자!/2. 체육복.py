def solution(n, lost, reserve):
    uniform = [1] * (n + 2)

    for i in lost:
        uniform[i] -= 1
    for i in reserve:
        uniform[i] += 1

    for i in range(1, n + 1):
        if uniform[i - 1] == 0 and uniform[i] == 2:
            uniform[i - 1: i + 1] = [1, 1]

        if uniform[i + 1] == 0 and uniform[i] == 2:
            uniform[i:i + 2] = [1, 1]

    return len([x for x in uniform[1:-1] if x > 0])


def solution(n, lost, reserve):
    s = set(reserve) & set(lost)
    l = set(lost) - s
    r = set(reserve) - s

    for i in sorted(r):
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)

    print(s)

    return n - len(l)