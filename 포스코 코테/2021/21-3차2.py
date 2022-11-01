n = int(input())

answer = []

if n<= 5 :
    answer = [0,2]
elif n== 6:
    answer = [1,2]
elif n==7 :
    answer = [2,2]
else :
    answer.append(n//7*2)
    answer.append(n//7*2+n%7)
print(answer)
