# N개의 수 수열, N-1연산자(덧셈,곱셈,나눗셈,뺄셈)
# 연산자 우선 순위 무시, 정수 나눗셈 몫
# 음수/양수 C++기준을 따름 => 양수로 바꾼뒤 몫을 취하고 음수로 바꿈
#식이 최대와 최소 프로그램 구하기
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
#연산자 값넣기
op_num = list(map(int, input().split()))
op_list = ['+','-','*','/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

#계산하기
'''
1.연산자는 지금 개수로 받음! 어떻게 섞을것인지?
2.숫자는 순서대로 이기 때문에 연산자에 따라 계산하면 됨
'''

maxnum = -1e9
minnum = 1e9
#순열활용

def solve():
    global maxnum, minnum
    for case in permutations(op,N-1):
        total = num[0]
        for j in range(1,N):
            if case[j-1] == '+':
                total +=num[j]
            elif case[j-1]=='-':
                total -= num[j]
            elif case[j-1]=='*':
                total *= num[j]
            elif case[j-1]=='/':
                total = int(total/num[j])
        if total > maxnum:
            maxnum = total
        if total < minnum:
            minnum = total
solve()
print(maxnum)
print(minnum)