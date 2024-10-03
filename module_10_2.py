from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_count = 100
        self.days_fought_count = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies_count > 0:
            self.enemies_count -= self.power
            self.days_fought_count += 1
            print(f'{self.name} сражается {self.days_fought_count} дней(дня), осталось {self.enemies_count} воинов\n')
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.days_fought_count} дней(дня)!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')