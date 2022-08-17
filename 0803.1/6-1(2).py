'''
1. 소문자로 변환/ 공백 특수문자 제거하고 나열
2. reversed랑 같은지 비교해서 T,F 출력
'''

import re

#문자열의 공백 제거한 리스트 만들기
words = input().strip().lower()
words = list(map(str, words.replace(' ', '')))


words_list = []

#특수문자 제거한 리스트 만들기 
for char in words:
    if re.sub('\W','',char): 
        #re.sub('패턴','바꿀문자열','문자열','바꿀횟수')/ 
        # \W => none word를 표현하며 알파벳+숫자+_ 가 아닌 문자열 의미
            words_list.append(char)

#펠린드롬 여부 판별
if words_list == list(reversed(words_list)):
    print(True)
else:
    print(False)