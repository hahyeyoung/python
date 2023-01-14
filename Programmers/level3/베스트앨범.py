#한번 다시 풀어보기
def solution(genres, plays):
    answer = []
    total = {}
    genres1 = {}

    for i in range(len(genres)):
        if genres[i] in total:
            total[genres[i]] += plays[i]
        else:
            total[genres[i]] = plays[i]
        if genres[i] in genres1:
            genres1[genres[i]].append([plays[i], i])
        else:
            genres1[genres[i]] = [[plays[i], i]]

    g_rank = sorted(total, key=total.get, reverse=True)

    for x in g_rank:
        p_rank = sorted(genres1[x], key=lambda x: (-x[0], x[1]))
        if len(p_rank) == 1:
            answer.append(p_rank[0][1])
        else:
            for i in range(2):
                answer.append(p_rank[i][1])
    return answer