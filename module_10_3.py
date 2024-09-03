from random import randint
from time import sleep
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            next_int = randint(50, 500)
            self.balance += next_int
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            print(f'Пополнение:{next_int}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            next_int = randint(50, 500)
            print(f'Запрос на {next_int}')

            if next_int <= self.balance:
                self.balance -= next_int
                print(f'Снятие: {next_int}. Баланс: {self.balance}')

            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
