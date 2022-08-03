#2. Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.

def is_prime(x):
    a=0
    for i in range (2,(x//2+1)):
        if x%i==0:
            a +=1
    if a<=0:
        print(True)
    else:
        print(False)
is_prime(int(input('Введите число от 0 до 1000:')))

# def is_prime(x):
#     a = list(range(1000))
#     a.remove(0)
#     a.remove(1)
#     # print(a)
#     for i in a:
#         for j in a:
#             if j % i == 0 and j != i:
#                 a.remove(j)
#     print(a)
#     return (x in a)
#     # if x in a:
#     #     return True
#     # else:
#     #     return False
# print(is_prime(int(input('Введите число от 0 до 1000:'))))

#функция должна вычислять простое число или нет, а вы это отдельно