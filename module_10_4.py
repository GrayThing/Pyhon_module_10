from threading import Thread
from random import randint
from time import sleep
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
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = [*tables]

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            free_tables = self.get_free_tables()
            if free_tables:
                free_tables[0].guest = guest
                print(f'{guest.name} сел(-а) за стол номер {free_tables[0].number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or len(self.get_free_tables()) < len(self.tables):
            for table in self.tables:
                if table.guest:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен')
                        table.guest = None
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start()

    def get_free_tables(self):
        return [table for table in self.tables if not table.guest]


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