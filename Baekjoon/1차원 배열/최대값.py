a = []

for i in range(9):
    a.append(int(input()))

maxnum = max(a)
print(max(a))
print(a.index(maxnum)+1)