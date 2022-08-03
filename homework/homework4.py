a = input('Enter a ten digit number: ')
result = ''
if len(a)==10:
    for i in a:
        if (int(i)%2)==0:
            result=result+i
        else:
            continue
else:
    print ('You entered an invalid number')
print (result)
# нет условия проверяющего что введенное число именно десятизначное