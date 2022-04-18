'''
후위표시법 *을 중심으로 계산할 수 있도록
'''
stack=[]
n = list(map(str,input().split()))
for i in n:
    stack.append(i)
    if stack[-1] == "*":
        b = int(stack[-3])*int(stack[-2])
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(b)
    elif stack[-1]=="+":
        c = int(stack[-3])+int(stack[-2])
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(c)
    elif stack[-1]=="-":
        d = int(stack[-3]) - int(stack[-2])
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(d)
print(stack[0])


'''
stack=[]
cal = []
sum = 0
n = list(map(str,input().split()))
for i in n:
    if i == '+' or i == '-' or i=='*':
        cal.append(i)
    else :
        stack.append(i)
print(stack)
'''