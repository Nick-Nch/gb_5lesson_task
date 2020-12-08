# 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f = open('task_5.2.txt')

lines = f.readlines()
print(len(lines), 'lines in text')
for num, line in enumerate(lines, start=1):
    print(num, 'string contains', len(line.split()), 'words')

f.close()
