'''
숫자의 개수 세는 함수 count
'''

A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))

for x in range(10):
    print(result.count(str(x)))