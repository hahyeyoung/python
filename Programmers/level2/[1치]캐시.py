def solution(cacheSize, cities):
    answer = 0
    i = 0
    cache = []
    if cacheSize == 0: #캐쉬가 비어있을 때 도시*5
        return len(cities)*5
    for c in cities:
        city = c.lower() #대소문자 구분하지 않는 조건
        if city in cache :
            cache.remove(city)
            cache.append(city)
            answer+=1
        else :
            answer+=5
            if i<cacheSize:
                cache.append(city)
                i +=1
            else :
                cache.pop(0)
                cache.append(city)
    return answer