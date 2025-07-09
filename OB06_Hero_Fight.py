# Импорт необходимых модулей
import random  # Для случайного выбора первого атакующего
import time  # Для создания задержек между ходами


# Класс Hero представляет игрового персонажа
class Hero:
    # Конструктор класса (инициализация героя)
    def __init__(self, name, health=100, attack_power=20):
        self.name = name  # Имя героя
        self.health = health  # Уровень здоровья (по умолчанию 100)
        self.attack_power = attack_power  # Сила атаки (по умолчанию 20)

    # Метод атаки другого героя
    def attack(self, other):
        other.health -= self.attack_power  # Уменьшаем здоровье противника
        # Выводим информацию об атаке
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")

    # Проверка, жив ли герой
    def is_alive(self):
        return self.health > 0  # Возвращает True, если здоровье > 0


# Класс Game управляет игровым процессом
class Game:
    # Конструктор класса (инициализация игры)
    def __init__(self, player_name):
        # Создаем героя для игрока
        self.player = Hero(player_name)
        # Создаем героя для компьютера
        self.computer = Hero("Компьютер")

    # Основной метод, запускающий игру
    def start(self):
        # Приветственные сообщения
        print("Начинается битва героев!")
        print(f"{self.player.name} vs {self.computer.name}")
        print("Битва начинается!\n")

        # Случайно выбираем кто атакует первым
        current_attacker = self.player if random.choice([True, False]) else self.computer
        round_num = 1  # Счетчик раундов

        # Основной игровой цикл (пока оба героя живы)
        while self.player.is_alive() and self.computer.is_alive():
            # Вывод информации о текущем состоянии
            print(f"\nРаунд {round_num}")
            print(f"{self.player.name}: {self.player.health} HP")
            print(f"{self.computer.name}: {self.computer.health} HP\n")

            # Логика атаки
            if current_attacker == self.player:
                self.player.attack(self.computer)  # Игрок атакует компьютер
                current_attacker = self.computer  # Передаем ход компьютеру
            else:
                self.computer.attack(self.player)  # Компьютер атакует игрока
                current_attacker = self.player  # Передаем ход игроку

            round_num += 1  # Увеличиваем номер раунда
            time.sleep(1)  # Пауза 1 секунда для удобства восприятия

        # Когда цикл завершен (один из героев мертв)
        self.declare_winner()  # Объявляем победителя

    # Метод для объявления победителя
    def declare_winner(self):
        print("\nБитва окончена!")
        # Проверяем кто победил
        if self.player.is_alive():
            print(f"{self.player.name} побеждает с {self.player.health} HP!")
        else:
            print(f"{self.computer.name} побеждает с {self.computer.health} HP!")


# Точка входа в программу
if __name__ == "__main__":
    # Приветствие
    print("Добро пожаловать в игру 'Битва героев'!")
    # Запрос имени игрока
    player_name = input("Введите имя вашего героя: ")
    # Создаем экземпляр игры
    game = Game(player_name)
    # Запускаем игру
    game.start()