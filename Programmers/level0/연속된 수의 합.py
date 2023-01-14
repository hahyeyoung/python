def solution(num, total):
    test = total//num
    return [i for i in range(test - (num-1)//2, test + (num + 2)//2)]