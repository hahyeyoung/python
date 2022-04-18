'''
많이 나오는 문제 괄호문제 꼭 다시 풀기!!!
'''

n = list(map(str, input().rstrip()))

def is_valid(s): ### 괄호가 안맞을때 함수
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
    if not stack:
        return True
    return False


def sol(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        else:
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2
                else:
                    tmp = 0
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j] == '(':
                            stack[-1] = tmp*2
                            break
                        else:
                            tmp += stack[-1]
                            stack.pop()
            else:
                if stack[-1] == '[':
                    stack[-1] = 3
                else:
                    tmp = 0
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j] == '[':
                            stack[-1] = tmp*3
                            break
                        else:
                            tmp += stack[-1]
                            stack.pop()
    return sum(stack)

if is_valid(n):
    print(sol(n))
else:
    print(0)


'''
stack = []
n = list(map(str, input().split()))
cnt = 0
cnt1 = 0
sum = 1
for i in n :
    stack.append(i)
    if i == '(' :
        cnt +=1
    elif i == ')' :
        if stack[-1] == '(':
            sum +=2
        else :
            sum *=2
    elif i == '[' :
        cnt1 +=1
    elif i == ']':
        if stack[-1] == '(':
            sum += 3
        else:
            sum *= 3
print(sum)
'''
