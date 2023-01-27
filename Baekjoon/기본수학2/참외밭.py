k = int(input())
max_h = 0
max_w = 0
max_h_index = 0
max_w_index = 0
temp = []
for i in range(6):
    num = list(map(int,input().split()))
    temp.append(num)
    if num[0] ==1 or num[0]==2:
        if max_w < num[1]:
            max_w = num[1]
            max_w_index =  i
    else :
        if max_h < num[1]:
            max_h = num[1]
            max_h_index = i
index_list = [temp[max_h_index - 1], temp[(max_h_index + 1) % 6], temp[max_w_index - 1],
              temp[(max_w_index + 1) % 6]]
test = 1
for i in temp:
    if i not in index_list:
        test *=i[1]

result = (max_w * max_h - test)*k
print(result)
