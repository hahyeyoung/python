import sys
from itertools import combinations

cb = list()
while True:
    s = list(map(int,sys.stdin.readline().split()))
    if s[0]==0:
        break

    cb.append(list(combinations(s[1:],6)))

for i in range(len(cb)):
    for j in cb[i]:
        print(' '.join([str(a) for a in j]))
    print()
