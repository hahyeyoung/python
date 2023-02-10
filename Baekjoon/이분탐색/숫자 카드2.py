N = int(input())
num = list(map(int,input().split()))
M = int(input())
test = list(map(int,input().split()))

num.sort()

def bs(l, target, start, end):
    if start > end:
        return 0
    mid = (start+ end)//2
    if l[mid] == target:
        return cnt.get(target)
    elif l[mid] > target:
        return bs(l,target,start, mid-1)
    else:
        return bs(l, target, mid+1, end)

cnt = {}
for i in num:
    if i in cnt:
        cnt[i]+=1
    else :
        cnt[i] = 1

for i in test:
    print(bs(num,i,0,len(num)-1), end=' ')



# import sys
# from collections import Counter
#
# M=int(sys.stdin.readline())
# list1=list(map(int,sys.stdin.readline().split()))
# N=int(sys.stdin.readline())
# list2=list(map(int,sys.stdin.readline().split()))
#
# c= Counter(list1)
#
# for i in list2:
#   if i in c:
#     print(c[i], end=' ')
#   else:
#     print(0, end=' ')
