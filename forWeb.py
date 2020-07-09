import json
import codecs
import time
import threading


f = codecs.open('static/data.json', 'r', 'cp1251')
time1 = time.time()
parsed_dict = json.load(f)


tbl = 5
min_char = 4
max_char = 7
words = set()
sets = []
table = []

for i in range(tbl):
    sets.append([])
    for j in range(tbl):
        sets[i].append(set())


def check_and_run(x, y, word, my_set, tp):
    if tp[x][y]:
        find_word(x, y, {'word': word['word'] + table[x][y], 'x': word['x'] + str(x), 'y': word['y'] + str(y)}, my_set, tp)


def find_word(x, y, word, my_set, tp):
    if len(word['word']) >= min_char:
        my_set.add(json.dumps(word, ensure_ascii=False))
    if len(word['word']) > max_char:
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


threads = []


def run_threads(stroka):
    # table = json.loads(stroka)["chars"]

    for i in range(tbl):
        table.append([])
        for j in range(tbl):
            table[i].append(stroka[i*tbl + j])

    # for bukva in stroka:
    #     table[tt // 5][tt % 5] = bukva
    #     tt = tt + 1
    print(table)
    for i in range(tbl):
        for j in range(tbl):
            print("Thread %s started" % (i * tbl + j))
            obj = {'word': table[i][j], 'x': str(i), 'y': str(j)}
            t = threading.Thread(target=find_word, args=(i, j, obj, sets[i][j], [
                [True, True, True, True, True],
                [True, True, True, True, True],
                [True, True, True, True, True],
                [True, True, True, True, True],
                [True, True, True, True, True]
            ]))
            threads.append(t)
            t.start()

    for i in threads:
        i.join()

    ret = []
    for i in range(tbl):
        for j in range(tbl):
            for word in sets[i][j]:
                try:
                    loaded = json.loads(word)
                    if parsed_dict[loaded["word"]]:
                        print(word)
                        ret.append(loaded)
                except KeyError:
                    pass
    return sorted(ret, key=lambda r: len(r["word"]), reverse=True)


