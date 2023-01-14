def solution(clothes):
    cloth = {}
    answer = 1

    for cl in clothes:
        if cl[1] in cloth.keys():
            cloth[cl[1]].append(cl[0])
        else:
            cloth[cl[1]] = [cl[0]]

    for value in cloth.values():
        answer *= len(value) + 1

    return answer - 1