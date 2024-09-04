from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        rand_time = randint(3, 10)
        sleep(rand_time)


class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = [table for table in args]

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while True:
            list_busy_table = [table.guest.name for table in self.tables if table.guest is not None]
            if len(list_busy_table) == 0:
                break

            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if table.guest is None  and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
            sleep(1)



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()



