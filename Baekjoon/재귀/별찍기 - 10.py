'''
3*3의 별모양이 그대로 크게 보이는 모양(다시 풀어보기)
ex)
***
* *
***

*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********
'''

def stars(n):
    map = []
    for i in range(3*len(n)):
        if i//len(n)==1:
            map.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
        else:
            map.append(n[i%len(n)]*3)
    return map
star = ["***","* *","***"]
n = int(input())
a = 0
while n != 3:
    n = int(n/3)
    a+=1
for i in range(a):
    star = stars(star)
for i in star:
    print(i)
