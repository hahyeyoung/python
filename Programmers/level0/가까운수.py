def solution(array, n):
    answer = 0
    array.sort()
    minus = [abs(i-n) for i in array]
    a = minus.index(min(minus))
    answer = array[a]
    return answer