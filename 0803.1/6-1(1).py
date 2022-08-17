'''
1. 공백,특수문자,대소문자 구분없이 나열
2. reverse랑 같은지 비교해서 T,F 출력
'''



words = input().strip().lower() #좌ㅜ 공백 제거 / 대문자를 소문자로 변환
words = list(map(str, words.replace(' ', ''))) #공백 없애고 list로 변환

words_list = [] 

for char in words:
    if char.isalpha: #특수문자를 제외한 문자들만 리스트에 넣으려고 했는데 , : 이런 요소들도 is alpha로 분류됨
            words_list.append(char)

if words_list.reverse() == words_list:
    print(True)
else:
    print(False)


