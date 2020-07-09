import codecs
import json

f = codecs.open('static/lop1v2.txt', 'r', 'cp1251')
s_lines = f.read().split('\n')
s_words = [parts.split('#')[0] for parts in s_lines]

json_string = {}
for word in s_words:
    if len(word) > 1 and not "-" in word:
        json_string[word] = True
with open('static/data.json', 'w', encoding='cp1251') as f:
    json.dump(json_string, f, ensure_ascii=False, indent=2)
