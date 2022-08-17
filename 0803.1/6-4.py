#단어만 리스트에 담기
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"

paragraph = paragraph.lower()
paragraph = paragraph.replace(',', '')
paragraph = paragraph.replace('.', '')

banned = ['hit']

p_list = list(map(str, paragraph.split()))

#금지단어가 포함되어 있으면 리스트에서 삭제
for word in p_list:
    if word in banned:
        p_list.remove(word)

#가장 많이 등장한 단어 찾기
max_word = max(set(p_list), key=p_list.count)

print(max_word)