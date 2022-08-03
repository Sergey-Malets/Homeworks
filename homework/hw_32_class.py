#Допишите несколько атрибутов в класс с прошлого задания, продемонстрируйте их работу

class Example:
    def print(self):
        print("Hello world")
    def suma(self,a,b):
        print(a+b)
    def multiply(self,a,b):
        print(a*b)
    def just_atribute(self):
        print('atribute')
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
    def __hash__(self):
        pass


print(str(Example))
# print(__eq__(Example))
print(hash(Example))
print(dir(Example))
ex = Example()
ex_1 = Example()
object_1 = Example()
ex_1.print()
object_1.suma(10,2)
object_1.multiply(int(input('first number:')),int(input('second number:')))
object_1.just_atribute()