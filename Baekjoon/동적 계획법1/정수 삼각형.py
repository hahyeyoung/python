n = int(input())
tray = []
for i in range(n):
    tray.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(len(tray[i])):
        if j==0:
            tray[i][j]=tray[i][j]+tray[i-1][j]
        elif j==len(tray[i])-1:
            tray[i][j]=tray[i][j]+tray[i-1][j-1]
        else:
            tray[i][j]=max(tray[i-1][j-1],tray[i-1][j])+tray[i][j]
print(max(tray[n-1]))