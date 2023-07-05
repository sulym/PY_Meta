import copy


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Triangle:
    def __init__(self,
                first_point: Point,
                second_point: Point,
                third_point: Point) -> None:
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point

    def __str__(self) -> str:
        return f"Triangle out of {self.first_point.x, self.first_point.y}, "\
            f"{self.second_point.x, self.second_point.y}, "\
            f"{self.third_point.x, self.third_point.y}"


def copy_point(point: Point) -> Point:
    return copy.copy(point)


def copy_triangle(triangle: Triangle) -> Triangle:
    return copy.deepcopy(triangle)
