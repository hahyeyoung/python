def solution(spell, dic):
    answer = 2
    word = ''
    spell = ''.join(sorted(spell))

    for i in dic:
        i = ''.join(sorted(i))
        if i == spell:
            answer = 1
    return answer

'''
다른사람풀이
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
    
    
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2
'''