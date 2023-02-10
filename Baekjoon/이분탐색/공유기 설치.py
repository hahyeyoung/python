N, C = map(int,input().split())
num = []
for i in range(N):
    num.append(int(input()))
num.sort()

def bs(num, start, end):
    while start <= end:
        mid = (start+end)//2
        current = num[0]
        cnt = 1
        for i in range(1, len(num)):
            if num[i] >= current+mid:
                cnt +=1
                current = num[i]
        if cnt >= C:
            global result
            start = mid+1
            result = mid
        else:
            end =mid -1
start = 1
end = num[-1]-num[0]
result =0

bs(num,start,end)
print(result)