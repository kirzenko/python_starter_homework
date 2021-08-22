#Задание 2 Напишите программу, которая запрашивает три целых числа a, b и x и выводит True,
# если x лежит между a и b, иначе – False.

a = int(input('Ведите число a = '))
b = int(input('Ведите число b = '))
y = int(input('Ведите число y = '))
if a < y < b  or b < y < a:
    print('True')
else: print('False')
