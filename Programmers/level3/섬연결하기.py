#크루스칼 알고르즘
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    bridge = set([costs[0][0]])
    while len(bridge)!=n:
        for i in costs:
            if i[0] in bridge and i[1] in bridge:
                continue
            if i[0] in bridge or i[1] in bridge:
                bridge.update([i[0],i[1]])
                answer+=i[2]
                break
    return answer