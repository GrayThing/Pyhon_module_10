import inspect
import math
from pprint import pprint


class Figure():
    sides_count = 0

    def __init__(self, colors: tuple, *sides_qty: int, filled=False):
        if self.__is_valid_sides(*sides_qty):
            self.__sides = [*sides_qty]
        else:
            self.__sides = [1 for _ in range(0, self.sides_count)]
        if self.__is_valid_color(*colors):
            self.__color = [*colors]
        else:
            self.__color = [0, 0, 0]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0:
            return False
        if not isinstance(r, int) and not isinstance(g, int) and not isinstance(b, int):
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
           self.__color = [r, g, b]
        else:
            print(f'Параметры не могут превышать значение 255 или быть меньше 0')

    def __is_valid_sides(self, *args):
        for side in args:
            if side <= 0 or not isinstance(side, int):
                return False
        if len(args) != self.sides_count:
            return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            print(f'Ошибка. Допустимое количество сторон {self.sides_count},'
                  f' внесено {len(new_sides)}')
            return
        for side in new_sides:
            if not isinstance(side, int):
                print(f'Сторона должна быть экземпляром класса int, получено {type(side).__name__}')
                return
        self.__sides = [*new_sides]


class Circle(Figure):
    sides_count = 1

    def __init__(self, colors: tuple, *sides_qty: int, filled=False):
        super().__init__(colors, *sides_qty, filled=filled)
        self.__radius = (self.get_sides()[0] / (2 * 3.14))

    def get_square(self):
        return self.get_sides()[0] ** 2 / (4 * 3.14)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = 0.5 * (sides[0] + sides[1] + sides[2])
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors: tuple, *sides_qty: int, filled=False):
        super().__init__(colors, *sides_qty, filled=filled)
        if len(sides_qty) == 1:
            self.set_sides(*[sides_qty[0] for _ in range(0, self.sides_count)])
        if len(sides_qty) > 1:
            self.set_sides([1 for _ in range(0, self.sides_count)])

    def get_volume(self):
        return self.get_sides()[0] ** 3


cube = Cube((255, 1, 1), 15)


def introspection_info(obj):
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    try:
        module = inspect.getmodule(obj).__name__
    except:
        module = __name__
    return {
        'Тип объекта': type(obj).__name__,
        'Атрибуты объекта': attributes,
        'Методы объекта': methods,
        'Модуль': module,
        'Встроенные методы': [attr for attr in dir(obj) if inspect.isbuiltin(getattr(obj, attr))]
    }


number_info = introspection_info(14)
pprint(number_info)

