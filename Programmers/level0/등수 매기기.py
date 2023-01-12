def solution(score):
    answer = []
    avg = []
    for i in score:
        avg.append(sum(i) // 2)
    sort_avg = sorted(avg, reverse=True)

    for i in avg:
        answer.append(sort_avg.index(i) + 1)
    return answer