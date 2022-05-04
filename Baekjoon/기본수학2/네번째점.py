'''
count 함수 활용하여 1개인 점들 넣기
'''

x_list = []
y_list = []

for i in range(3): #입력값
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
for j in range(3):
    if x_list.count(x_list[j])==1:
        x4 = x_list[j]
    if y_list.count(y_list[j])==1:
        y4 = y_list[j]
print(x4, y4)