from collections import Counter
N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
num.sort()
cnt = Counter(num).most_common(2)
print(round(sum(num)/len(num)))
print(num[N//2])
if len(num)> 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else :
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(num)-min(num))