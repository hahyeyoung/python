n = int(input())
a = [False, False] + [True]*(n-1)
num = []
for i in range(2, n+1):
    if a[i]:
        num.append(i)
        for j in range(2*i, n+1, i):
            a[j]= False
answer = 0
start, end = 0,0
while end<=len(num):
    temp = sum(num[start:end])
    if temp == n:
        answer +=1
        end +=1
    elif temp <n:
        end +=1
    else :
        start +=1
print(answer)