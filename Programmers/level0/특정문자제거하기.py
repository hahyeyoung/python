def solution(my_string, letter):
    answer = my_string.replace(letter,'')
    return answer
#실패한 풀이
    answer = ''
    # word = list(my_string)
    # for i in word:
    #     if letter == i:
    #         word.remove(i)
    # for i in word:
    #     answer+=i