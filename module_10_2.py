from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_enemy = 100
        count_days = 0

        while count_enemy > 0:
            count_enemy -= self.power
            count_days += 1
            print(f'{self.name} сражается {count_days} день(дня)..., осталось {count_enemy} воинов.')

            sleep(1)
        print(f"{self.name} одержал победу спустя {count_days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir_Galahad', 20)

first_knight.start()
sleep(0.1)
second_knight.start()

first_knight.join()
second_knight.join()
