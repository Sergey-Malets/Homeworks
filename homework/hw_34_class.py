#Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине слова,
# выводить все гласные, иначе согласные; если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе

class Homework:

    def ent(self):
        self.a = input('enter:')
        return self.a

    # def __init__(self):
    #     self.ent()
# пробовал через инит начинать ввод слов, но потом не итерировалось, а когда a = ex.ent() - то 2 раза просит ввод.
# причину почему нот дефайнд self.a так и не понял(оно ведь возвращается сразу с метода ent...

    def func_len(self):
        return len(a)

    def stroka(self):
        gl = 0
        sogl = 0
        all_gl = []
        all_sogl = []
        list_gl = ['e', 'u', 'i', 'o', 'a']
        for i in a:
            if i in list_gl:
                gl += 1
                all_gl.append(i)
            else:
                sogl += 1
                all_sogl.append(i)
        if (gl * sogl) <= ex.func_len():
            print(all_gl)
        else:
            print(all_sogl)

    def chislo(self):
        summ=0
        for i in a:
            if int(i) % 2 == 0:
                summ += int(i)
        print(summ * ex.func_len())

    def proverka(self):
        if a.isalpha():
            ex.stroka()
        elif a.isdigit():
            ex.chislo()
        else:
            print('enter error.')

ex = Homework()

while True:
    a = ex.ent()  # без этой строчки не хотело итерировать self.a,не могу понять почему?!
    ex.proverka()
    if a == '`':
        break



