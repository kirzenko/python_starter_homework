# Использовать на практике все методы словарей на своем примере.


dict_1 = {'a': 3, 'b': 0, 'c': 4, 'd': -3}
dict_11 = {'L': 10, 'K': 20, 'P': 30}


def func_1():
    a = dict_1['a']
    print(a)


def func_2():
   dict_1['b'] = 100
   print(dict_1)


def func_3():
    if 'c' in dict_1:
        print('ok')


def func_4():
    print(dict_1.items(), dict_1.keys())


def func_5():
    dict_1.update(dict_11)
    print(dict_1)


def func_6():
    print(len(dict_11))


def func_7():
    if 23 in dict_11:
       print('Yes')
    else:
       print('No')


def func_8():
    print(dict_1.get('d'))


def func_9():
    dict_1.update(dict_11)
    print('обновление словаря', dict_1)


def main():
    func_1()
    func_2()
    func_3()
    func_4()
    func_5()
    func_6()
    func_7()
    func_8()
    func_9()



if __name__ == "__main__":
    main()



