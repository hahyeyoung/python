N = int(input())
num = list(map(int,input().split()))
M = int(input())
num1 = list(map(int,input().split()))

num.sort()

for i in num1:
    front, end = 0, N-1
    isExist = False

    while front <= end :
        mid = (front + end)//2
        if i == num[mid]:
            isExist = True
            print(1)
            break
        elif i > num[mid]:
            front = mid+1
        else :
            end = mid -1

    if not isExist:
        print(0)

