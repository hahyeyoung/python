def solution(chicken):
    answer = 0
    copon = 0

    answer += chicken // 10
    copon = chicken // 10 + chicken % 10

    while (copon >= 10):
        answer += copon // 10
        copon = copon // 10 + copon % 10

    return answer