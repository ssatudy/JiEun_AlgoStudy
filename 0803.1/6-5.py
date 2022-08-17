words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
result = {}
for word in words:
    w = ''.join(sorted(word))
    result[w] = result.get(w,[]) + [word]

values_list = list(result.values())

print(values_list)