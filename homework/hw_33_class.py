#Допишите по 2 динамических и статических свойства в класс с предыдущего задания. Продемонстрируйте их работу
class Car:
    # Статические поля (переменные класса)
    default_color = 'Black'
    default_weight = 1400
    default_brand = 'Volkswagen'
    default_model = 'Golf'

    def __init__(self, color, model, brand, weight ):
        # Динамические поля (переменные объекта)
        self.color = color
        self.model = model
        self.brand = brand
        self.weight = weight

    def turn_on(self):
        pass

    def ride(self):
        pass

car_object = Car('red', 'x3','BMW',1600)
my_car = Car('black','golf','volkswagen',1300)

print(car_object.default_brand)
print(car_object.color)
print(my_car.weight)
print(dir(Car))
print(Car.__dict__)
print(car_object.__dict__)