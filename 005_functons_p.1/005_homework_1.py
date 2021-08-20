# Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если
# имя не указано, она должна выводить приветствие для пользователя с Вашим именем.


def hello(name='Python'):
    if not name:
        return print('Hello, Oleksandr')
    print('Hello, ', name, '!')


hello('Python')
hello('')


if __import__ == '__main__':
    hello()