# Создайте программу, вычисляющую значение такой функции y = f(x):
# y = cos(3x) при −π ≤ x ≤ π
# y = х при x < -π или x > π
# Значение x вводится пользователем. Используйте оператор if-else,
# зависящий от результата сравнения; используйте оператор or;
# выведите на экран соответствующее условию значение y.

import math
x = float(input('Введите х: '))

if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)

elif x < -math.pi or x > math.pi:
    y = x
print(f'y = {y}')
#Кращий варіант!!тернарний оператор
#import math
#x = float(input('Введите х: '))
#print('y= ', math.cos(3 * x)) if -math.pi <= x <= math.pi else print('y = ', x)
