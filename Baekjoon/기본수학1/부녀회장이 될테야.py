t = int(input())

for i in range(t):
    floor = int(input()) #층
    ho = int(input()) #호
    floor0 = [x for x in range(1,ho+1)] #0층

    for k in range(floor):
        for j in range(1,ho):
            floor0[j]+= floor0[j-1]
    print(floor0[-1])

