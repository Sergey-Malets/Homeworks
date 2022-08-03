# #Есть словарь песен группы Depeche Mode
# violator
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова
songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
s = songsdict.values()
#print(s)
print(sum(s))
l=list()
# key = str()
# value = float()
for key, value in songsdict.items():
    if value>5:
        l.append(key)
print(l)
k=list()
v=list()
for key, value in songsdict.items():
    if " " in key:
        continue
    else:
        k.append(key)
        v.append(value)
d=dict(zip(k,v))
print(d)
#попробуйте отсортировать по значению. В интернете пишут что нужна функция lambda которую пока не изучали.
list_val = list(songsdict.items())
#print (list_val)
list_val.sort(key=lambda x : x[1])
#print (list_val)
for i in list_val:
    print(i[0],':',i[1])
