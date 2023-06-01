import statistics


class ListStatistics:
    
    def __init__(self, numbers: list) -> None:
        self.__numbers = numbers

    def calculate_statistics(self) -> dict:
        new_dict = {}
        new_dict["min_value"] = self.__get_min_value()
        new_dict["max_value"] = self.__get_max_value()
        new_dict["average"] = self.__get_average()
        new_dict["median"] = self.__get_median()
        return new_dict
    
    def __get_min_value(self) -> int:
        return min(self.__numbers)

    def __get_max_value(self) -> int:
        return max(self.__numbers)
    
    def __get_average(self) -> float:
        return sum(self.__numbers) / len(self.__numbers)

    def __get_median(self) -> float:
        return statistics.median(self.__numbers)

rap = ListStatistics([1,2,3])
a = rap.calculate_statistics()
print(a)


### m ###

class ListStatistics:
    def __init__(self, numbers: list) -> None:
        self.__numbers = sorted(numbers)

    def __get_min_value(self) -> int:
        return self.__numbers[0]

    def __get_max_value(self) -> int:
        return self.__numbers[-1]

    def __get_average(self) -> float:
        return sum(self.__numbers) / len(self.__numbers)

    def __get_median(self) -> int:
        if len(self.__numbers) % 2 == 0:
            return (
                self.__numbers[len(self.__numbers) // 2 - 1]
                + self.__numbers[len(self.__numbers) // 2]
            ) / 2
        return self.__numbers[len(self.__numbers) // 2]

    def calculate_statistics(self) -> dict:
        return {
            "min_value": self.__get_min_value(),
            "max_value": self.__get_max_value(),
            "average": self.__get_average(),
            "median": self.__get_median(),
        }
