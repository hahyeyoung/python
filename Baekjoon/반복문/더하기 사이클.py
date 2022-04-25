N = int(input())
num= N
cycle = 0
while True:
    a = num//10
    b = num%10
    c = (a+b)%10
    num = (b*10)+c

    cycle +=1
    if (num ==N):
        break
print(cycle)