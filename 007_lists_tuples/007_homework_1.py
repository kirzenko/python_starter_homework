# Есть список а = [2, 4, 65, 32, 2, 6, 0, -1, 3]. Вывести все значения меньше 5 в консоль.


def func_1():
    list_a = [2, 4, 65, 32, 2, 6, 0, -1, 3]
    final_list = []
    for i in list_a:
        if i < 5:
            final_list.append(i)
    return final_list


def main():

    print(func_1())


if __name__ == "__main__":
    main()