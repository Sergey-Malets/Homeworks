#Создайте функцию, которая принимает на вход неограниченное количество позиционных и именованных аргументов,
# в качестве результата функция должна возвращать только позиционные аргументы с нечетными индексами и ключевые,
# значения которых являются строками

def func(*args,**kwargs):
    #args=(1,2,3,4,5,2,1,3,5,4,9)
    args = input('введите позиционные через пробел')
    args = tuple(args.split())
    kwargs={'a':'qwerty','b':2,'c':3,'qwerty':['q'],1:'au'}
    #kwargs = input('введите ключевые через пробел:')
    print(args[1::2])
    #kwargs = dict(zip(kwargs.split(),kwargs.split()))
    #print(kwargs)
    for key,value in kwargs.items():
        if type(value)==str:
            print(key)
func()
