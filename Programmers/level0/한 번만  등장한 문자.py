def solution(s):
    word = list(s)
    stack = []
    remove_list = []
    for i in word:
        if i not in stack:
            stack.append(i)
        else :
            remove_list.append(i)
            continue
    for i in remove_list:
        if i in stack :
            stack.remove(i)
    stack.sort()
    return ''.join(stack)

'''
다른 사람 풀이
def solution(s):
    answer = ''
    list_s = list(s)
    list_s.sort()
    for i in list_s:
        if list_s.count(i)==1:
            answer+=i
    return answer
'''