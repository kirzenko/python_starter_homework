# Напишите функцию, которая меняет значение глобальной переменной.

A, B, C = 57, 12, 14


def function():
    global A, B, C
    A, B, C = 2, 3, 4



def main():
    function()
    print(A, B, C)


if __name__ == '__main__':
    main()






























