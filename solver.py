import json
import codecs
import time
import threading


f = codecs.open('static/data.json', 'r', 'cp1251')
time1 = time.time()
parsed_dict = json.load(f)
stringi = 'отялбмухааантноклшрыуврйг'
t = 0
table = [
    ['а', 'б', 'в', 'я', 'п'],
    ['г', 'д', 'о', 'о', 'п'],
    ['ж', 'а', 'в', 'д', 'а'],
    ['ж', 'з', 'к', 'а', 'у'],
    ['ж', 'з', 'к', 'а', 'к']
]
for i in stringi:
    table[t // 5][t % 5] = i
    t = t + 1

print(table)

tbl = len(table)
min_char = 4
max_char = 8
words = set()
sets = []
tp = []

for i in range(tbl):
    sets.append([])
    tp.append([])
    for j in range(tbl):
        sets[i].append(set())
        temp = []
        for k in range(tbl):
            temp.append(True)
        tp[i].append([])
        tp[i][j] = temp


def check_and_run(x, y, word, my_set, tp):
    if tp[x][y]:
        find_word(x, y, word + table[x][y], my_set, tp)


def find_word(x, y, word, my_set, tp):
    if len(word) >= min_char:
        my_set.add(word)
    if len(word) > max_char:
        return True
    tp[x][y] = False
    xx = x + 1
    yy = y
    if xx < tbl:
        check_and_run(xx, yy, word, my_set, tp)

        yy = y + 1
        if yy < tbl:
            check_and_run(xx, yy, word, my_set, tp)

        yy = y - 1
        if yy >= 0:
            check_and_run(xx, yy, word, my_set, tp)

    xx = x - 1
    yy = y
    if xx >= 0:
        check_and_run(xx, yy, word, my_set, tp)

        yy = y + 1
        if yy < tbl:
            check_and_run(xx, yy, word, my_set, tp)

        yy = y - 1
        if yy >= 0:
            check_and_run(xx, yy, word, my_set, tp)

    xx = x
    yy = y + 1
    if yy < tbl:
        check_and_run(xx, yy, word, my_set, tp)
    yy = y - 1
    if yy >= 0:
        check_and_run(xx, yy, word, my_set, tp)
    tp[x][y] = True

    return True

#
# for i in range(tbl):
#     for j in range(tbl):
#         find_word(i, j, table[i][j], words)

threads = []


for i in range(tbl):
    for j in range(tbl):
        print("Thread %s started" % (i * tbl + j))
        t = threading.Thread(target=find_word, args=(i, j, table[i][j], sets[i][j], [
            [True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True]
        ]))
        threads.append(t)
        t.start()

# print(len(words))
for i in threads:
    i.join()

print('--------------------------------------')
for i in range(tbl):
    for j in range(tbl):
        for word in sets[i][j]:
            try:
                if parsed_dict[word]:
                    words.add(word)
            except KeyError:
                pass
print(sorted(words, key=len, reverse=True), len(words))

time2 = time.time()
print(time2-time1)