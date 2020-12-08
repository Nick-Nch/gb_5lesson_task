# 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('file_5.txt', 'w+') as f:
    num = input('Enter whole numbers separated by a space: ')
    f.writelines(num)
    my_numb = num.split()
    print('Sum of entered numbers:', sum(map(int, my_numb)))

