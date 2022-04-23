'''
공백없이 숫자 리스트에 한글자씩 넣기
import sys
sys.stdin.readline().rstrip()
'''
import sys

N = int(input())
num = list(sys.stdin.readline().rstrip())
sum = 0

for i in range(N):
    sum += int(num[i])
print(sum)