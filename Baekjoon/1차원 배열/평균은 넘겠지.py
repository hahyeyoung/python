N = int(input())

for i in range(N):
    grade = list(map(int, input().split()))
    over = 0
    for j in range(1,len(grade)) :
        average = (sum(grade)-grade[0])/(len(grade)-1)
        if grade[j] > average :
            over +=1
    rate = over/grade[0]*100
    print(f'{rate:.3f}%')
