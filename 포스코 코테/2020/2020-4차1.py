arr = list(map(int,input().split()))
answer = 0

while arr!=[1] :
    cnt = 1
    result = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt +=1
        elif arr[i] != arr[i+1]:
            result.append(cnt)
            cnt = 1
    answer+=1
    arr = result
print(answer)


