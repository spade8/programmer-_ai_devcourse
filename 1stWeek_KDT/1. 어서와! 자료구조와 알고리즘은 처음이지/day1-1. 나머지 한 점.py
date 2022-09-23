def solution(v):
    answer = []
    x = []
    y = []
    for dot in v:
        if dot[0] in x:
            x.remove(dot[0])
        else:
            x.append(dot[0])
        if dot[1] in y:
            y.remove(dot[1])
        else:
            y.append(dot[1])
    answer.append(x[0])
    answer.append(y[0])

    return answer