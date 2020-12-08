# 3
# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('task_5.3.txt') as f:
    lines = f.readlines()
    payments = []
    for line in lines:
        name, payment = line.split()
        payments.append(float(payment))
        if float(payment) < 20000:
            print(line)
print('Average profit:', sum(payments) / len(payments))
