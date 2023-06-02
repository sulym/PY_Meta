from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def do_work(self) -> None:
        pass
        
    @abstractmethod
    def stop_work(self) -> None:
        pass


class Truck(Machine):
    def do_work(self) -> None:
        print("Truck starts working")

    def stop_work(self) -> None:
        print("Truck stopped working")


class Bulldozer(Machine):
    def do_work(self) -> None:
        print("Bulldozer starts working")

    def stop_work(self) -> None:
        print("Bulldozer stopped working")
    

class Excavator(Machine):
    def do_work(self) -> None:
        print("Excavator starts working")

    def stop_work(self) -> None:
        print("Excavator stopped working")


def build() -> None:
    truck_one = Truck()
    bull = Bulldozer()
    excav = Excavator()

    truck_one.do_work()
    bull.do_work()
    excav.do_work()

    truck_one.stop_work()
    bull.stop_work()
    excav.stop_work()


print(build())