def solution(n):
    n1 = format(n, 'b')
    count_n = n1.count('1')
    while(1):
        n +=1
        test = format(n,'b')
        count_test = test.count('1')
        if count_n == count_test :
            break
    return n