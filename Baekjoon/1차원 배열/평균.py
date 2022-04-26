N = int(input())
grade = list(map(int, input().split()))
maxgrade = max(grade)
sum = 0
for i in range(N):
    sum = sum + grade[i]/maxgrade*100
print(sum/N)