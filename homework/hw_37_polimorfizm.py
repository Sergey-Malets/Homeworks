#Придумайте свой примеры видов полиморфизма. Прикрепите скриншоты или файл с ними.

class Papa:

    def __init__(self,name, age):
        self._name = name
        self._age = age

    def deti(self):
        print(f'{self._name} стал отцом в {self._age} лет')

vova = Papa('Vova',21)
vova.deti()

class Son(Papa):

    def __init__(self, name, age=None):
        super().__init__(name, age)
        self._name = name
        self._age = age
        self._name_wife = 'Hanna'
        if self._age is not None:
            sergey.deti()
        else:
            print(f'У {self._name} нет детей.')

    def deti(self):
        print(f'{self._name} стал отцом в {self._age} лет.')
        print(f'Жену зовут {self._name_wife}.')


sergey = Son('Sergey')
# sergey.deti()

def show_polymorphism():
    for i in [Papa, Son]:
        print('-------')
        object = i(input('Name:'),input('Age:'))
        object.deti()

show_polymorphism()
