# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке
import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))


class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super().__init__(lang, letters)

        # __letters_num = len(self.letters) #когда это свойство динамическое всё ОК, почему?!
        # print(__letters_num)

    # __letters_num = len(self.letters) #вот почему??name 'self' is not defined

    @property
    def __letters_num(self):
        return len(self.letters)

    @__letters_num.setter
    def nevazhno(self, __letters_num):
        self.__letters_num = __letters_num


    def is_en_letter(self, letter):
        if letter in self.letters:
            print(f'{letter} относится к английскому алфавиту.')
        else:
            print(f'{letter} не относится к английскому алфавиту.')

    def letters_num(self):
        print(self.__letters_num)

    @staticmethod
    def example():
        print('Hello world!')


# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке

if __name__ == '__main__':
    obj = EngAlphabet('En', string.ascii_uppercase)
    obj.print()
    obj.letters_num()
    obj.is_en_letter('F')
    obj.is_en_letter('Щ')
    EngAlphabet.example()
