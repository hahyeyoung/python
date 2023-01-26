num = list(map(int,input().split()))

answer = 0
stack = []

for i in range(len(num)):
    if num[i] not in stack:
        stack.append(num[i])
    else:
        stack.append(num[i]+1)
        answer +=1
print(stack)


# stack = []
#
# for i in num:
#     if i not in stack:
#         stack.append(i)
#     else:
#         stack.append(i+1)
#         answer +=1
# print(stack)