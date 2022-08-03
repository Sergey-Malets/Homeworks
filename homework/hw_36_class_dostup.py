class Urovni_dostupa:
    public = 12
    _protected = 9
    __privat = 2

    def __init__(self):
        a = (Urovni_dostupa.public - Urovni_dostupa._protected)**Urovni_dostupa.__privat
        print(a)

ex = Urovni_dostupa()

print((ex.public - ex._protected)**ex._Urovni_dostupa__privat)
print(Urovni_dostupa.__dict__)
print(ex.__dict__)