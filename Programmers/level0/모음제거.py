def solution(my_string):
    answer = ''
    word = list(my_string)
    for i in word:
        if 'a'==i or 'e'==i or 'i'==i or 'o'==i or 'u' ==i:
            answer +=''
        else :
            answer += i
    return answer

#다른사람풀이

'''
def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string
'''