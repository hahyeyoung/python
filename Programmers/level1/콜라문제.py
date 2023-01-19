def solution(a, b, n):
    answer = 0

    while (n >= a):
        test = n % a
        n = (n // a) * b
        answer += n
        n += test
    return answer