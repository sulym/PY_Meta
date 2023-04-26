import math


class Point:
    # write you code here
    points = []
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        Point.points.append(self)

    
    def distance_to_origin(self) -> float: 
        # повертає відстань від точки до початку координат
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)
    
    
    def distance_to_point(self, point: None) -> float:
        # приймає точку point і повертає відстань від поточної точки до point
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)

    def distance_to_x_axis(self: None) -> int:
        # повертає відстань до осі Х
        return round(abs(self.y))
    
    def distance_to_y_axis(self: None) -> int:
        # повертає відстань до осі Y
        return round(abs(self.x))
    
    def find_closest_point(self) -> "Point":
        # Перевіряємо, чи містить список точок self.points якісь елементи.
        if not self.points:
            return None
        
        min_distance = None
        closest_point = None
        for other_p in self.points:
            if other_p is not self:
                distance = self.distance_to_point(other_p)
                if min_distance is None:
                    min_distance = distance
                    closest_point = other_p
                elif distance < min_distance:
                    min_distance = distance
                    closest_point = other_p
            
        return closest_point

# створені точки
point_1 = Point(3, 4)
point_2 = Point(-5, -1)
point_3 = Point(4, 4)
point_4 = Point(1, 1)

# методи виклику до точок
point_distanc_origin = point_1.distance_to_origin()
pointt_distanc_point = point_1.distance_to_point(point_2)
distanc_to_x = point_1.distance_to_x_axis()
distanc_to_y = point_1.distance_to_y_axis()
closest_poin = point_1.find_closest_point()
all_points = Point.points

print(point_distanc_origin)
print(pointt_distanc_point)
print(distanc_to_x)
print(distanc_to_y)
print(closest_poin.x, closest_poin.y)
print(all_points)

"""
Напиши клас Point. Його метод __init__ приймає та зберігає x, y координати точки. 
Всі створені екземпляри повинні зберігатись в списку points - атрибуті класа Point.

Клас Point повинен надавати такі методи:

distance_to_origin - повертає відстань від точки до початку координат
distance_to_point - приймає точку point та повертає відстань від поточної точки до point
distance_to_x_axis - повертає відстань до осі Х
distance_to_y_axis - повертає відстань до осі Y
find_closest_point - повертає найближчу точку до поточної серед інших створених точок,
якщо інших точок немає - повертає None
"""