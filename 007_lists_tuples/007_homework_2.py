# Создайте список и введите его значения.
# Найдите наибольший и наименьший элемент списка, а также сумму и среднее арифметическое его значений.

first_list = [1, 2, 3, -4, 122, 12, 3, 15, -34]


def main():
    print('минимальное значение = ', min(first_list))
    print('максимальное значние = ', max(first_list))
    print('сумма = ', sum(first_list))
    print('среднее арифметическое = ', sum(first_list) / len(first_list))


if __name__ == "__main__":
    main()












