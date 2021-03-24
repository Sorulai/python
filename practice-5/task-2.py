# -*- coding: UTF-8 -*-
with open('task-2.txt') as my_file:
    # content = my_file.readline()
    count_line = 0
    count_words = 0

    for line in my_file:
        count_line +=1
        print(f'В {count_line} строке {len(line.split())} слов')

    print(f'Строк в файле = {count_line}')




