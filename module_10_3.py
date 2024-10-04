from threading import Thread, Lock
import random
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for turn in range(100):
            old_balance = self.balance
            self.balance += random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {self.balance - old_balance}. Баланс: {self.balance}\n')
            sleep(0.001)

    def take(self):
        for turn in range(100):
            r_int = random.randint(50, 500)
            print(f'Запрос на {r_int}\n')
            if r_int <= self.balance and not self.lock.locked():
                self.balance -= r_int
                print(f'Снятие: {r_int}. Баланс: {self.balance}\n')
            else:
                self.lock.acquire()
                print(f'Запрос отклонён, недостаточно средств\n')
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


