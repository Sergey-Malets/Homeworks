#Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

def conter_dec(func):
    def wrapper(a):
        wrapper.count +=1
        res = func(a)
        name = func.__name__
        count = wrapper.count
        print(f'{name} была вызвана: {count} раз(а)')#.format(func.__name__, wrapper.count))
        return res
    wrapper.count=0
    return wrapper

@conter_dec
def function(b):
    return b
print(function(2))
print(function(4))
print(function(7))


# def counter_dec(n):
#     n=0
#     if True:
#         n+=1
#     print(f'функция вызвана {n} раз.')
#     return counter_dec
#
# @counter_dec
# def function(arg):
#     x=2
#     print(arg,x)
# function(5)


    