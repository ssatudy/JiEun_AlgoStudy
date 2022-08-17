
logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

'''
chars = []
chars_num = []
for i in logs:
    not_identi = i[5:]
    if not_identi.isdigit():
        chars_num.append(i)

    else:
        chars.append(i)


total_list = chars + chars_num
print(total_list)

=> not_identi 의 뛰어쓰기를 없애야 if문에서 리스트가 제대로 구분됨
'''

logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

chars = []
chars_num = []
for i in logs:
    not_identi = i[5:].replace(' ','')
    if not_identi.isdigit():
        chars_num.append(i)

    else:
        chars.append(i)

chars_num.sort()
chars.sort()

total_list = chars + chars_num
print(total_list)

#정렬 기준을 식별자를 제외하고 해야되는데, 식별자를 포함한 기준으로 정렬을 하니까, 순서가 예시랑 틀리게나옴