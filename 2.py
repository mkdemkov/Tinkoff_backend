from collections import defaultdict
dictionary = defaultdict(int)
s = input()
dictionary['s'] = 0
dictionary['h'] = 0
dictionary['e'] = 0
dictionary['r'] = 0
dictionary['i'] = 0
dictionary['f'] = 0
# заполним словарь, обойдя исходную строку за O(n), где n - длина строки
for ch in s:
    if ch in dictionary:
        dictionary[ch] += 1

min_count = len(s)
dictionary['f'] //= 2
# обойдем заполненный словарь
for key, val in dictionary.items():
    if val < min_count:
        less_symbol = key
        min_count = val

# если какой-то из символов слова sheriff встретился 0 раз в исходной строке
if not min_count:
    print(0)
else:
    print(min_count)