'''
등차수열: 숫자와 숫자의 사이의 간격이 동일한 숫자의 나열
첫번째수와 두번째숫자의 차가 두번쨰수와 마지막수의 숫자와 같으면 한수를 더함
'''

n = int(input())
han = 0
for i in range(1,n+1):
    if i<100:
        han +=1
    else :
        num = list(map(int,str(i)))
        if num[0]-num[1] == num[1]-num[2]:
            han+=1
print(han)