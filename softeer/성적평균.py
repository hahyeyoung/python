import sys
N,K = map(int,input().split())
grade = list(map(int, input().split()))
for i in range(K):
    a, b = map(int, input().split())
    avg  = 0
    sum_num = 0
    di = 0
    for j in range(a,b+1):
        sum_num += grade[j-1]
        di +=1
    avg = float(sum_num/di)
    print(f'{avg:.2f}')