'''
짝수는 3번째칸에 있어야 함
홀수는 2번째칸에 먼저 있어야 함
'''

def hanoi(n, a,b,c) :
    if n==1:
        move.append([a,c])
    else :
        hanoi(n-1,a,c,b)
        move.append([a,c])
        hanoi(n-1,b,a,c)

move = []
hanoi(int(input()), 1,2,3)

print(len(move))
print("\n".join([' '.join(str(i) for i in row) for row in move]))






