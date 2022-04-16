'''
리스트가 스택의 역할
append 함수를 활용, 스택은 선입후출이기에
reverse()함수 활용
'''

n = int(input())
s = list(map(str, input()))
s.reverse() #스택으로 넣기 위해
stack = []
for i in range(0, n):
    stack.append(s[i])
    if (i+1)%3 ==0 and i != n-1:
        stack.append(',')
stack.reverse()
print("".join(stack))