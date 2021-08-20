# Напишите  функцию,  которая  будет  возвращать  результат  наибольшего  общего  делителя  двух
# чисел, переданных в параметры.


def function(a, b):
    if a > b:
        r = a % b
        if r == 0:
            return b
        else:
            return function(b, r)
    if a < b:
        r = b % a
        if r == 0:
            return a
        else:
            return function(a, r)
print(function(14,7))


def main():
    function(14,7)


if __name__ == '__main__':
    main()
