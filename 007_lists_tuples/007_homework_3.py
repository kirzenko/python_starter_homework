# Напишите программу, которая вводит с клавиатуры текст и выводит
# отсортированные по алфавиту слова данного текста.


# сортировка букв по алфавиту получается, а как сделать сортировку слов?
# text = input('Введите текст: ')
# list_1 = sorted(text)
# print(list_1)


def func():
    text = input('Введите текст: ')
    list_1 = text.lower().split(' ')
    text = sorted(list_1)
    final_list = []
    for i in text:
        if i:
            final_list.append(i)
    return final_list


def main():

    print(func())


if __name__ == "__main__":
    main()






