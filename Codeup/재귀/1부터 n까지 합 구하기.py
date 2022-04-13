'''
전역변수 global
# 인풋받으며 바로 넣어야 재귀함수 효능가능
'''

'''
1) 코드 실패 : 범위 벗어남
n = int(input())
sum = 0
def hap(n):
    global sum
    if n!=1:
        hap(n-1)
    sum += n
hap(n)
print(sum)
'''
import sys
sys.setrecursionlimit(1000000)


# 2번째 안
def hap(n):
    if n<=1:
        return 1
    return hap(n-1)+n
print(hap(int(input())))
