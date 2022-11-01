from itertools import permutations


def solution(k, dungeons):
    dun_num = len(dungeons)
    answer = 0
    for perm in permutations(dungeons, dun_num):
        hp = k
        count = 0
        for pm in perm:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
        if count > answer:
            answer = count

    return answer