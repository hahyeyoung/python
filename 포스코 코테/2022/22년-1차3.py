m = 4
v = [3, 2, 3, 1]

stack = []
matrix = [m]*m
for i in v:
    for j in range(len(matrix)):
        if matrix[j] !=0 and matrix[j]>=i:
            matrix[j] = matrix[j]-i
            stack.append(i)
            break
        else:
            continue
answer = 0
for i in matrix :
    if i != m :
        answer +=1
print(answer)



