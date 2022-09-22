from collections import deque
def solution(s):
    answer = 0
    que = deque(s)

    for i in range(len(s)):
        temp = que.popleft()
        que.append(temp)
        if check(que) == True:
            answer += 1
    return answer

def check(que):
    stack = []
    for c in que:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            x = stack.pop()

            # 밑 코드는 괄호 짝 검사
            if c == ')' and x != '(':
                return False
            elif c == ')' and x != '(':
                return False
            elif c == '}' and x != '{':
                return False

    return len(stack) == 0

