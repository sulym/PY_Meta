import math


class NumberInfo:
    def __init__(self, number: any) -> None:
        self._number = number

    @property
    def number(self) -> any:
        return self._number
    
    @number.setter
    def number(self, value: any) -> any:
        self._number = value

    @property
    def len_digits(self) -> int:
        return len(str(int(self._number)))
    
    @property
    def is_integer(self) -> bool:
        return isinstance(self._number, int)
    
    @property
    def is_float(self) -> bool:
        return isinstance(self._number, float)

    @property
    def decimal(self) -> int:
        if isinstance(self._number, float):
            return len(str(self._number).split(".")[1])
        return 0
    
    @property
    def is_positive(self) -> bool:
        return self._number > 0

    @property
    def is_natural(self) -> bool:
        return isinstance(self._number, int) and self._number > 0
    
    @property
    def is_prime(self) -> bool:
        integer_part = int(self._number)
        if isinstance(self._number, float):
            return False
        if integer_part < 2:
            return False
        for i in range(2, int(math.sqrt(integer_part)) + 1):
            if integer_part % i == 0:
                return False
        return True


a = NumberInfo(123.1234)
print(a.is_prime)


### m ###

class NumberInfo:
    def __init__(self, number: int) -> None:
        self._number = number

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        self._number = value

    @property
    def is_prime(self) -> bool:
        if self._number < 2:
            return False
        if self.is_integer:
            for i in range(2, self._number):
                if self._number % i == 0 and self._number != 2:
                    return False
        if self.is_float:
            return False
        return True

    @property
    def len_digits(self) -> int:
        return len(str(int(self._number)))

    @property
    def is_integer(self) -> bool:
        return isinstance(self._number, int)

    @property
    def is_float(self) -> bool:
        return isinstance(self._number, float)

    @property
    def decimal(self) -> int | float:
        if self.is_integer:
            return 0
        return len(str(self._number).split(".")[-1])

    @property
    def is_positive(self) -> bool:
        return True if self._number > 0 else False

    @property
    def is_natural(self) -> bool:
        return True if self.is_positive and self.is_integer else False