import math


class Figure:
    sides_count = 0

    def __init__(self, *args):
        self.__color = []
        self.__sides = []
        self.filled = False
        sides = []
        for i in args:
            if isinstance(i, tuple):       # присваивание rgb __color
                for rgb in i:
                    self.__color.append(rgb)

            else:
                sides.append(i)

        if len(sides) != self.sides_count:
            for j in range(0, self.sides_count):
                self.__sides.append(1)
        else:
            self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True

        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False

        if len(sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        summ = 0
        for side in self.__sides:
            summ += side

        return summ

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides.clear()
            for side in new_sides:
                self.__sides.append(side)


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __init__(self, *args):
        super().__init__(*args)
        self.__radius = round(super().get_sides()[0] / (3.14 * 2), 2)

    def get_square(self):
        return round(3.14 * (self.__radius ** 2), 2)


class Triangle(Figure):
    sides_count = 3
    __height = 0

    def __init__(self, *args):
        super().__init__(*args)
        self.__height = self.get_height()

    def get_height(self):
        p = super().__len__() / 2
        sizes = self.get_sides()
        return round((math.sqrt(p * (p-sizes[0]) * (p-sizes[1]) * (p-sizes[2]))) / sizes[0], 2)

    def get_square(self):
        sizes = self.get_sides()

        return round((self.__height * sizes[0]) / 2, 2)


class Cube(Figure):
    sides_count = 12
    __sides = []

    def __init__(self, *args):
        super().__init__(*args)

        if len(args) == 2:
            for i in range(0, self.sides_count):
                self.__sides.append(args[-1])
        else:
            self.__sides = self.get_sides()

    def set_sides(self, *new_sides):
        if self._Figure__is_valid_sides(*new_sides):
            self.__sides.clear()
            for side in new_sides:
                self.__sides.append(side)

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())