'''
다시풀기
'''


d=[]
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
for i in range(19):
    d[i] = list(map(int, input().split()))

n = int(input())
for i in range(n) :
  x,y=map(int, input().split())  ##input값 여기까지 입력됨

  for j in range(1,20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0
for a in range(len(d)):
    print(' '.join(map(str,d[a])))