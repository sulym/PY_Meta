
class Point:
    color = "red"
    circle = 2

a = Point()
b = Point()
a.x = 1
a.y = 2

b.x = 10
b.y = 20

print(Point.__dict__)