
s = []

for i in range(9):
    s.append(list(map(int,input().split())))

num = 0
x,y = 0, 0

for i in range(9):
    for j in range(9):
        if s[i][j]> num :
            num = s[i][j]
            x = i
            y = j

print(num)
print(x+1,y+1)