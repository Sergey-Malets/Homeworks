#Задача№2
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

d = {a:(a+3)*2 for a in range(1,5)}
print(d)
k=1
v=1
for key,value in d.items():
    k = k*key
    v = v*value
print(d.items())
print(k, v)