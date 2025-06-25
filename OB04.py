# Задание:
# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
#
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и
# возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

# Решение:

# Создаем класс Animal и атрибуты name и age
class Animal():
# Создаем метод инициализации __init__
    def __init__(self, name, age):
# Привязываем характеристики к классу
        self.name = name
        self.age = age
# Создаем метод (функцию) make_sound
    def make_sound(self):
        pass

# Создаем метод (функцию) eat
    def eat(self):
# Выводим информацию о том, что name поел
        print(f'{self.name} поел')

# Создаем классы, которые будут наследовать данные

# Класс Bird (птицы)
class Bird(Animal):
# Переопределяем метод make_sound
    def make_sound(self):
# Выводим информацию
        print('Курлык-Курлык')

# Класс Mammals (млекопитающие)
class Mammal(Animal):
# Переопределяем метод make_sound
    def make_sound(self):
# Выводим информацию
        print('Мяу')

# Класс Reptile (рептилии)
class Reptile(Animal):
# Переопределяем метод make_sound
    def make_sound(self):
# Выводим информацию
        print('ффшшфшшшфшшшш')

# Работаем над полиморфизмом

# Создаем функцию animal_sound
def animal_sound(animals):
# перебираем список животных в цикле for
    for animal in animals:
# Вызываем для каждого конкретного животного функцию make_sound
        animal.make_sound()

# Создаем новый класс Zoo, у него не будет наследия
class Zoo():
    def __init__(self):
# Создаем списки животных (animals) и сотрудников (staff)
        self.animals = []
        self.staff = []

# Создаем методы для добавления животных и сотрудник в списки
    def add_animal(self, animal):
# Добавляем данные через функцию append
        self.animals.append(animal)
# Вывод информации
        print(f'Животное {animal.name} заселилось в зоопарк')
# Создаем аналог для сотрудников
    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f'Сотрудник {new_staff} устроен в штат зоопарка')

# Создаем классы для сотрудников Zookeeper и Veterinarian
class ZooKeeper():
# Функция кормить конкретных животных
    def feed_animal(self, animal):
# Выводим данные
        print(f'Сотрудник покормил - {animal.name}')


class Veterinarian():
    def heal_animal(self, animal):
        print(f'Ветеринар вылечил {animal.name}')



# Создаем объекты классов по животным, зоопарку, сотрудникам

bird1 = Bird("Кеша", "2")
mammal1 = Mammal('Бобик', '1')
reptile1 = Reptile('Кобра', '3')

zoo = Zoo()

keeper = ZooKeeper()
veterinarian = Veterinarian()

# Начнем вызывать функции (добавляем их в зоопарк)

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

# Объекты вывод звуков животных
animal_sound(zoo.animals)

# Вывод действий сотрудников
keeper.feed_animal(mammal1)
veterinarian.heal_animal(reptile1)