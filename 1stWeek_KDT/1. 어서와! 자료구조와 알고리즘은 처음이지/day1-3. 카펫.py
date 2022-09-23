def solution(brown, red):
    sum_side = (brown + 4) // 2
    mul_side = brown + red
    answer = []
    for i in range(1, sum_side):
        if i * (sum_side - i) == mul_side:
            answer.append(i)
            answer.append(sum_side - i)
            break

    answer.sort(reverse=True)
    return answer