class Car:
    def __init__(self, comfort_class: int,
                clean_mark: int, brand: str
                ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                average_rating: float, count_of_ratings: int
                ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return round(cost, 1)

    def calculate_washing_price(self, car: Car) -> float:
        result = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * (self.average_rating / self.distance_from_city_center))

        return round(result, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        cost = ((self.average_rating * self.count_of_ratings + rating)
                / (self.count_of_ratings + 1))
        self.average_rating = round(cost, 1)
        self.count_of_ratings += 1
        

ford = Car(2, 1, 'Ford')
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')


wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)

income = wash_station.serve_cars([bmw, audi, mercedes])
ws_cost = wash_station.calculate_washing_price(ford)
rs = wash_station.rate_service(5)
print(income)
print(ws_cost) 
print(wash_station.average_rating)
print(wash_station.count_of_ratings)

# You own a car washing station. Washing cost calculation takes a lot of time, and you decide to automate this calculation. 
# The washing cost will depend on car comfort class, car cleanness degree, 
# wash station average rating and wash station distance from the center of the city.

# Create class Car, its __init__ method takes and stores 3 arguments:

# comfort_class - comfort class of a car, from 1 to 7
# clean_mark - car cleanness mark, from very dirty - 1 to absolutely clean - 10
# brand - brand of the car
# Create class CarWashStation, its __init__ method takes and stores 4 arguments:

# distance_from_city_center - how far station from the city center, from 1.0 to 10.0
# clean_power - clean_mark to which this car wash station washes (yes, not all stations can clean your car completely)
# average_rating - average rating of the station, from 1.0 to 5.0, rounded to 1 decimal
# count_of_ratings - number of people who rated
#CarWashStation should have such methods:

#1. serve_cars - method, that takes a list of Car's, washes only cars with clean_mark < clean_power of wash station and 
# returns income of CarWashStation for serving this list of Car's, rounded to 1 decimal:
#So, only bmw was washed, because audi.clean_mark > wash_station.clean_power, and bmw.clean_mark has changed, because we washed it.

#If audi.clean_mark was below wash_station.clean_power then audi would have been washed as well and the income would have raised:

#2. calculate_washing_price - method, that calculates cost for a single car wash, 
#cost is calculated as: car's comfort class * difference between wash station's clean power and
#car's clean mark * car wash station rating / car wash station distance to the center of the city,
#returns number rounded to 1 decimal;

#3. wash_single_car - method, that washes a single car, so it should have clean_mark equals wash station's clean_power,
#if wash_station.clean_power is greater than car.clean_mark;

#4.rate_service - method that adds a single rate to the wash station,
#and based on this single rate average_rating and count_of_ratings should be changed: