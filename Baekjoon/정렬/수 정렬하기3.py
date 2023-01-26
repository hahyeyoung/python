# import sys
# N = int(sys.stdin.readline())
# num = []*10001
# for i in range(N):
#     num.append(int(sys.stdin.readline()))
#
# num.sort()
# for i in num:
#     print(i)

import sys
N = int(sys.stdin.readline())
num = [0]*10000
for i in range(N):
    a = int(sys.stdin.readline())
    num[a-1] +=1

for i in range(10000):
    if num[i] !=0:
        for j in range(num[i]):
            print(i+1)