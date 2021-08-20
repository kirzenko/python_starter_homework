# Создайте программу, которая проверяет, является ли палиндромом введённая фраза.
# не понял как это сделать , нашел подобную и делал по примеру

def palindrome(word='ротор', i=0):
    if i == len(word):
        return word[0] == word[-1]

    elif word[i] == word[-i - 1]:
        return palindrome(word, i + 1)

    else:
        return False


def main():
    print(palindrome())


if __name__ == '__main__':
    main()





















