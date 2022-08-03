# Задание 1
# Простейший калькулятор c введёнными двумя числами вещественного типа.
#  Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
#  Обработать ошибку: “Деление на ноль”
#  Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def sum(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):
    if b == 0:
        return ("Деление на ноль невозможно")
    else:
        return a/b

while True:
    choice = input('Введи операцию (сумма=1, разница=2, умножение=3, деление=4, выход=0):')
    if choice == '1':
        a = float(input("введи первое число:"))
        b = float(input("введи второе число:"))
        print(sum(a,b))
    elif choice == '0':
        break
    elif choice=='2':
        a = float(input("введи первое число:"))
        b = float(input("введи второе число:"))
        print(subtract(a, b))
    elif choice=='3':
        a = float(input("введи первое число:"))
        b = float(input("введи второе число:"))
        print(multiply(a, b))
    elif choice=='4':
        a = float(input("введи первое число:"))
        b = float(input("введи второе число:"))
        print(divide(a, b))

