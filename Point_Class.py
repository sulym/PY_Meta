import math


class Point:
    # write you code here
    points = []
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        Point.points.append(self)

    
    def distance_to_origin(self) -> float: # повертає відстань від точки до початку координат
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)
    
    
    def distance_to_point(self, point: None) -> float: # приймає точку point і повертає відстань від поточної точки до point
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)

    def distance_to_x_axis(self: None) -> int: # повертає відстань до осі Х
        return round(abs(self.y))
    
    def distance_to_y_axis(self: None) -> int: # повертає відстань до осі Y
        return round(abs(self.x))


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


print(point_distanc_origin)
print(pointt_distanc_point)
print(distanc_to_x)
print(distanc_to_y)
print()

