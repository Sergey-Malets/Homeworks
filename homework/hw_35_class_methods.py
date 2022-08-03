#Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса

class Methods:
    atribut = 12
    @staticmethod
    def static():
        print('Это статический метод')

    @classmethod
    def class_met(cls):
        print(cls.atribut)
        #print(atribut) - я думал если у этого метода есть доступ к атрибутам класса, то принтанет, но не найден. не понятно
        print ('это классовый метод')

    def just_method(self,b):
        print(b*2)
object_1 = Methods()

Methods.static()
Methods.class_met()
object_1.just_method('MA')