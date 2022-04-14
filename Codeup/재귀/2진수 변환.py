'''
bin = 이진수
result = format(n,'b')
oct = 8진수
hex = 16진수
'''
result = []
def change(n):
    global result
    if n == 1  :
        result.append(1)
        return 1
    elif n == 0:
        result.append(0)
        return 0
    else :
        change(n//2)
        result.append(n%2)
        return result

change(int(input()))
print("".join(map(str,result)))


''' 기본코드 for문을 사용한 코드
def change(n):
    result = format(n,'b')
    print(result)
    return result

print(change(int(input())))
'''