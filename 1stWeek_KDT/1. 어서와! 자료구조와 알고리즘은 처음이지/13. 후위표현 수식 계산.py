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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for char in tokenList:
        if char in prec:  # 연산자,"(" 일때
            if opStack.size() == 0 or char == "(":
                opStack.push(char)
            else:  # 스택에 있는 연산자들 중 현재의 연산자보다 우선 순위가 더 큰 경우 모두 pop
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[char]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                opStack.push(char)

        elif char == ")":  # 괄호가 닫힐때
            while True:
                pop_result = opStack.pop()
                if pop_result == "(":
                    break
                else:
                    postfixList.append(pop_result)
        else:  # 피연산자 일때
            postfixList.append(char)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
    }
    opStack = ArrayStack()
    answer = 0
    for op in tokenList:
        if op in prec:
            operand_a = opStack.pop()
            operand_b = opStack.pop()
            if op == '*':
                opStack.push(operand_b * operand_a)
            if op == '/':
                opStack.push(operand_b / operand_a)
            if op == '+':
                opStack.push(operand_b + operand_a)
            if op == '-':
                opStack.push(operand_b - operand_a)
        else:
            opStack.push(op)
    answer = opStack.pop()

    return answer


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val