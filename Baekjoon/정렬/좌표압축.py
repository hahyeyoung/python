import sys
input = sys.stdin.readline

n = int(input())
dic = {}

num = list(map(int, input().split()))
num1 = sorted(set(num))

for i in range(len(num1)):
    dic[num1[i]] = i

for j in num:
    print(dic[j], end=' ')