# Есть словарь: d = {‘a’:3, ‘b’:0, ‘c’:4, ‘d’:-3}. Найти самое большое число из значений словаря.


def func():
    dict_1 = {'a': 3, 'b': 0, 'c': 4, 'd': -3}
    a1 = max(dict_1, key=dict_1.get)
    print(a1)


def main():
    func()


if __name__ == "__main__":
    main()


