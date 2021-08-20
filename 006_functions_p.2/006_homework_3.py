# Создайте  программу-калькулятор,  которая  поддерживает  четыре  операции:  сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет,  что  хочет  завершить  выполнение  программы.  Каждая  операция  должна  быть
# реализована  в  виде  отдельной  функции.  Функция  деления  должна  проверять  данные  на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.

# не могу понять почему цикл не работает?
def choose_operation():
    while True:
        choice = input('''
     Выберите необходимую операцию:
     1. sum
     2. sub
     3. mult
     4. div
     ''')
        if choice == 'exit':
            break


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
     print('Деление на ноль') if b == 0 else print('а / b = ', a / b)


def main():
    a = float(input('введите а: '))
    b = float(input('введите b: '))
    choice = input('''
         Выберите необходимую операцию:
         1. sum
         2. sub
         3. mult
         4. div
            ''')

    if choice == '1':
        result = sum(a, b)

    elif choice == '2':
        result = sub(a, b)

    elif choice == '3':
        result = mult(a,b)

    elif choice == '4':
        result = div(a,b)

    else:
        choice = input('''
     Выберите необходимую операцию:
     1. sum
     2. sub
     3. mult
     4. div
     ''')

    print(result)



if __name__ == '__main__':
    main()