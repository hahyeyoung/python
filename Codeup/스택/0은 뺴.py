'''
pop 맨위에 빼기
'''

stack=[]
n = int(input())
for i in range(0,n):
    a = int(input())
    if a == 0:
        stack.pop()
    else :
        stack.append(a)
print(sum(stack))