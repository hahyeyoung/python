while True :
    n = input().split('\n')
    stack = []
    if n[0] == '.':
        break
    for i in n[0]:
        if i=='(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')
    stack.clear()

