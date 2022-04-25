'''
빠르게 입력받는 법
Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()
'''
import sys

N = int(sys.stdin.readline())
sum = []

for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    sum.append(a+b)

for i in range(N):
    print(sum[i])