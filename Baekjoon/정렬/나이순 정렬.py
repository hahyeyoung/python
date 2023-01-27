n = int(input())
people = []
for i in range(n):
    a = list(input().split())
    people.append(a)
people.sort(key=lambda x: int(x[0]))

for i,j in people:
    print(i,j)