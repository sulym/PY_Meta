class RockBand:
    # write your code here
    def __init__(self, name: str, members: list) -> None:
        self.name = name
        self.members = members

    def add_new_member(self, new_member: str) -> None:
        if new_member in self.members:
            print(f"{new_member} is already in the band!")
        else:
            self.members.append(new_member)

    def __add__(self, others: None) -> None:
        return RockBand(
                name=self.name + " " + others.name + " United",
                members=set(self.members + others.members)
                )

first_band = RockBand("First", ["Ivan", "Sergey"])
second_band = RockBand("Second", ["Sergey", "Max"])

first_band.add_new_member("Ivan")
united = first_band + second_band

print(united.name, united.members) # "First Second United" ["Ivan", "Sergey", "Max"]

##### M #####

from __future__ import annotations


class RockBand:
    def __init__(self, name: str, members: list) -> None:
        self.name = name
        self.members = members

    def add_new_member(self, new_member: str) -> None:
        if new_member not in self.members:
            self.members.append(new_member)
        else:
            print(f"{new_member} is already in the band!")

    def __add__(self, other: RockBand) -> RockBand:
        members = []
        members.extend(self.members)
        for member in other.members:
            if member not in members:
                members.append(member)
        band_name = f"{self.name} {other.name} United"
        return RockBand(name=band_name, members=members)

    def __iadd__(self, other: RockBand) -> None:
        for member in other.members:
            if member not in self.members:
                self.members.append(member)
