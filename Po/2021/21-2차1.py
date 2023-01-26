'''
기준
좋음  보통    나쁨 매우나쁨
0~30  31~81  81~150 151
0~15  16~35  36~75  76
'''
# 보통, 보통/ 보통, 보통 / 좋음, 좋음 / 나쁨, 나쁨(1)/ 보통,좋음(1)/ 좋음(1)
mongi = [[78, 20], [42, 33], [5, 1] ,[99, 55], [56, 10], [5, 5]]
mask = 0
check = 0
day =0
for i,j in mongi:
    if i>= 81 or j>=36 : #나쁨
        if check == 0:
            mask +=1
            check +=1
            day +=1
        else :
            day +=1
    elif i>=151 or j>=76:
        mask +=1
        check = 0
    elif i<81 or j<36 :
        if day !=0:
            day +=1

    if day == 3:
        day = 0
        check = 0

print(mask)