import math
def solution(progresses, speeds):
    answer = []
    period = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        period.append(day)

    answer.append(1)
    for i in range(1, len(period)):
        if period[i] <= period[i - 1]:
            period[i] = period[i - 1]
            answer[-1] += 1
        else:
            answer.append(1)

    return answer