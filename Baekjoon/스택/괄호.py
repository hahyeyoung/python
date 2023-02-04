n = int(input())
stack = []
for i in range(n):
    word = list(input())
    for j in word :
        if j== '(':
            stack.append(j)
        elif j == ')':
            if stack :
                stack.pop(-1)
            else :
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else :
            print('NO')
    stack.clear()