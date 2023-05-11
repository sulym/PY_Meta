class LowerPrime:
    def __init__(self, number: int) -> None:
        self.number = number
        self.primes = [n for n in range(2, number) if self.is_prime(n)]
        self.index = 0
        
        # Метод __iter__ определяет,
        # что объект LowerPrime является итератором,
        # возвращает себя же при вызове функции iter().
    def __iter__(self) -> "LowerPrime":
        self.index = 0
        return self
    
        # Метод __next__ является основной частью итератора и определяет,
        # какие элементы будут возвращаться при итерации.
        # он возвращает следующее простое число, начиная с конца списка primes,
        # Если список был полностью перебран, то метод вызывает исключение StopIteration.
    def __next__(self) -> "LowerPrime":
        if self.index < len(self.primes):
            res = self.primes[::-1][self.index]
            self.index += 1
            return res
        raise StopIteration
    
    # Метод is_prime является вспомогательным методом,
    # который проверяет, является ли число простым.
    # Он используется в генераторе списка простых чисел в методе __init__.
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
num = 11

echo = LowerPrime(num)

iterator = iter(echo)
print(next(iterator))
print(next(iterator))
print(next(iterator))


### M ###

#from __future__ import annotations
#from typing import Union


class LowerPrime:
    def __init__(self, number: int) -> None:
        self.number = number
        self.current_number = number

    def __iter__(self) -> LowerPrime:
        self.current_number = self.number
        return self

    def __next__(self) -> Union[int, StopIteration]:
        for num in range(self.current_number - 1, 1, -1):
            if self.is_prime(num):
                self.current_number = num
                return num
        raise StopIteration

    @staticmethod
    def is_prime(number: int) -> bool:
        for divisor in range(2, number // 2 + 1):
            if number % divisor == 0:
                return False
        return True