# 1
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('task_5.1.txt', 'w+')
line = input('Введите текст: ')

while line:
    f.writelines(line + '\n')
    line = input('Введите текст: ')
    if not line:
        break
f.close()

with open('task_5.1.txt',) as f:
    content = f.readlines()
    print(content)
