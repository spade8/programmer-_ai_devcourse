
def solution(participant, completion):
    dict = {}
    for name in participant:
        dict[name] = dict.get(name, 0) + 1

    for name in completion:
        dict[name] -= 1

    dnf = [k for k, v in dict.items() if v > 0]

    answer = dnf[0]
    return answer