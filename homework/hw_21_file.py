#Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность
a=input('Введите 2 числа через пробел:')
#a=a.split()
f = open('input.txt','w')
f.write(a)
f.close()
f = open('input.txt','r')
b = f.readline()
#print(b)
b = b.split() #конвертирую в список для итерации
#print(type(b))
r=0
for i in b:
    r = int(i)-r
    #print(r)
f.close()
r = r*-1
print(r) #вывод в консоль для проверки
f = open('output.txt','w')
f.write(str(r))
f.close()