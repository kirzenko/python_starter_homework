# Даны две строки. Выведите на экран символы, которые есть в обоих строках.

def func():
   str_1 = 'В словаре не может быть двух элементов с одинаковыми ключами.'
   str_2 = 'Однако могут быть одинаковые значения у разных ключей.'

   set_11 = set(str_1)
   set_21 = set(str_2)
   set_11.intersection(set_21)
   set_31 = set_11.intersection(set_21)
   print(set_31)


def main():
    func()


if __name__ == "__main__":
    main()



