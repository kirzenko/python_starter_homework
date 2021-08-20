# В предложении “Hello world” заменить все буквы “o” на “a” , а буквы “l”  на “e”.

str = 'hello world!'

result = ''
i = 0

while i < len(str):
    if str[i] == 'o':
        result += 'a'
    elif str[i] == 'l':
        result += 'e'
    else:
        result += str[i]
    i += 1
print(result)

#for

result_2 = ''
for i in range(len(str)):
    if str[i] == 'o':
       result_2 += 'a'
    elif str[i] == 'l':
        result_2 += 'e'
print(result)