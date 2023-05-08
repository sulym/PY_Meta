import math
from typing import Union


class Vector:

    def __init__(self, x_vect: int, y_vect: int) -> None:
        self.x = round(x_vect, 2)
        self.y = round(y_vect, 2)

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

# Добавление двух векторов, возвращает вектор.
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

# Вычитание двух векторов возвращает вектор.
    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

# Умножение вектора на число возвращает другой вектор.
# Умножение вектора на вектор возвращает скалярный продукт.
    def __mul__(self, other: Union[int, float, "Vector"]
                ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

# Принимает start_point- кортеж координат точки, начало вектора,
# end_point- кортеж координат точки, конец вектора. 
# Возвращает вектор.
    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

# Возвращает длину вектора.
    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Возвращает нормализованную копию вектора.
    def get_normalized(self) -> "Vector":
        mag = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(self.x / mag, self.y / mag)

# Принимает vectorи возвращает угол между текущим вектором
# и vector в целых градусах.
    def angle_between(self, other: "Vector") -> int:
        scalar_vector = self * other
        length_one = self.get_length()
        length_too = other.get_length()
        return round(math.degrees
                     (math.acos(scalar_vector / (length_one * length_too))))

# Возвращает угол между текущим вектором и положительной осью Y.
    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return abs(round(angle_deg))

# Принимает degreesцелое число градусов вращения.
# Он возвращает повернутый вектор на degrees.
    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(new_x, new_y)


vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 + vector2
print(vector3)
print(isinstance(vector3, Vector))

vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 - vector2
print(vector3)
print(isinstance(vector3, Vector))

vector1 = Vector(2, 4)
vector2 = vector1 * 3.743
print(vector2)
print(isinstance(vector2, Vector))

vector1 = Vector(2.11, 4.55)
vector2 = Vector(-3.51, 10.33)
dot_product = vector1 * vector2
print(dot_product)
print(isinstance(dot_product, float))

start_point = (5.2, 2.6)
end_point = (10.7, 6)
vector = Vector.create_vector_by_two_points(start_point, end_point)
print(vector)
print(isinstance(vector, Vector))

vector = Vector(2, 4)
print(vector.get_length())

vector1 = Vector(13, -4)
vector2 = Vector(-6, -11)
print(vector1.angle_between(vector2))

vector = Vector(33, 8)
print(vector.get_angle())

vector = Vector(33, 8)
vector2 = vector.rotate(45)
print(vector2)

# https://github.com/mate-academy/py-vector-class