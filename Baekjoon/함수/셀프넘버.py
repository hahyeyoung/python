def selfnumber(n):
    n = n+ sum(map(int,str(n)))
    return n

nonSelfNum = set()

for i in range(1,10000):
    nonSelfNum.add((selfnumber(i)))

for j in range(1,10001):
    if j not in nonSelfNum:
        print(j)