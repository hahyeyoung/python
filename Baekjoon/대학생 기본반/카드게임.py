color = set()
num = []
result = 0
for i in range(5):
    A, B = input().split()
    color.add(A)
    num.append(int(B))

num.sort()
num_charge = set()
check = False
for i in range(len(num) - 1):
    num_charge.add(num[i + 1] - num[i])
if len(num_charge) == 1 :
    check = True

#색깔이 모두 같을 경우
if len(color) == 1:
#1) 숫자가 연속
    if check == True:
        result = max(num)+900
    else : #2) 색깔만 모두 같음
        result = max(num)+500
else : #아닐경우
    if check == True :
        result = max(num)+400
    else:
