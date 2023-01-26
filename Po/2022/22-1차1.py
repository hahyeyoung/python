lottery = [[1, 0], [35, 0], [1, 0], [100, 1], [35, 1], [100, 1], [35, 0], [1, 1], [1, 1]]

lottery.sort(key = lambda x:(x[0]))
people = []
sum_people = []
temp = 0
for i,j in lottery :
    if i not in people :
        people.append(i)
        temp = 0
    if j == 0 :
        temp +=1
    else :
        temp +=1
        sum_people.append(temp)
if len(people) == 0:
    print(0)
else :
    print(sum(sum_people)//len(people))






# lottery.sort(key = lambda x:(x[0]))
# people = 1
# sum_people = 0
# a = lottery[0][0]
# for i,j in lottery:
#     if a == i :
#         if j == 0:
#             sum_people += 1
#     else :
#         people +=1
#         sum_people +=1
#         a = i
# print(people)
# print(sum_people)
# if sum_people ==0:
#     print(0)
# else :
#     print(sum_people//people)