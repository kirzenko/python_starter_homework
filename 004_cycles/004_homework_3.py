#Создайте программу, которая рисует на экране прямоугольный треугольник указанной пользователем высоты.
height = int(input('Введите высоту прямоугольного треугольникa: '))
for row in range(height + 1):
    for column in range(height):
        if height < column:
            print('*', end='')
        else:
            print('-', end='')
    for column in range(height):
        if row > column:
            print('*', end='')
        else:
            print('-', end='')
    print()

# правильный вариант

size = int(input('please write size of triangle: '))

for a in range(size + 1):
    for b in range(a):
        print('*', end='')
    print()
