X = list(input().split())
Y = list(input().split())

answer = []

for i in Y:
    if i not in X:
        if i not in answer :
            answer.append(i)
    else :
        continue
print(answer)
