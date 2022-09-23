class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''

    for char in S:
        if char in prec:  # 연산자,"(" 일때
            if opStack.size() == 0 or char == "(":
                opStack.push(char)
            else:  # 스택에 있는 연산자들 중 현재의 연산자보다 우선 순위가 더 큰 경우 모두 pop
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[char]:
                        answer += opStack.pop()
                    else:
                        break
                opStack.push(char)

        elif char == ")":  # 괄호가 닫힐때
            while True:
                pop_result = opStack.pop()
                if pop_result == "(":
                    break
                else:
                    answer += pop_result
        else:  # 피연산자 일때
            answer += char

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer