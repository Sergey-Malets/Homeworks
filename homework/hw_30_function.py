#Задание 2
# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.

a = (1,2,4,6,'qwerty','привет')
b = [1,2,3,'qwe',3,'rty',(1,2,333,'asd')]
c = 12345678
d = 'qwerty u asdfg@! 123'

def func(*args):
    if type(*args) is tuple:
        n=0
        l=0
        #print(args)
        for i in args:
            for j in i: #двойная итерация так как кортеж в кортеже, и по другому не придумал как достать
                if type(j) is str:
                    n+=1
                    for k in j:
                        if k.isalpha: #почему спецсимволы Trueкают, не должны ведь
                            l+=1
        print(f'В кортеже {n} слов длинной {l} букв')
    elif type(*args)is list:
        letters = 0
        numbers = 0
        args = list(*args) #если это не сделать то аргумент не раскладывается на состовляющие
        for i in args: #сюда нельзя с символом *
            #print(i)
            if type(i) is str:
                letters = letters+len(i)
            elif type(i) is int: #сразу я сюда вписал or float,но тогда tuple почему-то шел по этому пути
                numbers = numbers+len(str(i)) # лен не применяется к числам, поэтому перевод в строку
            elif type(i) is tuple:
                for j in i:
                    #print(j)
                    if type(j) is str:
                        letters = letters + len(j)
                    elif type(j) is int or float:
                        numbers = numbers + len(str(j))
        print(f'в списке {letters} букв, {numbers}цифр')
        #print(len(args))
    elif type(*args)is int: #почему args это кортеж и как его отделить от скоб?
        n = 0
        args = list(str(*args)) #так замудрено потому что: 'int' object is not iterable
        # args = ','.join(args)
        #print (args)
        for i in args:
            if int(i)%2>0:
                n+=1
        print (f'В числе {n} нечетных цифр')
    elif type(*args)is str:
        n=0
        #print(args)
        for i in args:
            for j in i:
                if j.isalpha():
                    n+=1
        print(f'В строке {n} букв.')




    else:
        print('no')
func(a)
func(b)
func(c)
func(d)
# x = '!@#$%^&*('
# if x.isalpha:
#     print(True)