from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self.__musical_instrument = musical_instrument

    def get_rating(self):
        pass

    def player_info(self):
        pass

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self.__musical_instrument}")


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.__favourite_dish = favourite_dish

    def get_rating(self):
        pass

    def player_info(self):
        pass

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.__favourite_dish}")


class ElfRanger(Elf):
    def __init__(self,
                nickname: str,
                musical_instrument: str,
                bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self.__bow_level = bow_level

    def player_info(self) -> None:
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self.__bow_level} level")

    def get_rating(self) -> int:
        return self.__bow_level * 3


class Druid(Elf):
    def __init__(self,
                nickname: str,
                musical_instrument: str,
                favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self.__favourite_spell = favourite_spell

    def player_info(self) -> None:
        print(f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.__favourite_spell}")

    def get_rating(self) -> int:
        return len(self.__favourite_spell)


class DwarfWarrior(Dwarf):
    def __init__(self,
                nickname: str,
                favourite_dish: str,
                hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.__hummer_level = hummer_level

    def player_info(self) -> None:
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.__hummer_level} level")

    def get_rating(self) -> int:
        return self.__hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self,
                nickname: str,
                favourite_dish: str,
                skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.__skill_level = skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill of the {self.__skill_level} level")

    def get_rating(self) -> int:
        return self.__skill_level


def calculate_team_total_rating(players_list: list[Player]) -> int:
    count = 0
    for i in players_list:
        count += i.get_rating()
    return count


def elves_concert(players_list: list[Elf]) -> str:
    for i in players_list:
        i.play_elf_song()


def feast_of_the_dwarves(players_list: list[Dwarf]) -> int:
    for i in players_list:
        i.eat_favourite_dish()
        


ranger = ElfRanger(
    nickname="Nardual Chaekian",
    musical_instrument="flute",
    bow_level=7
)

team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]

elves = [
    Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
    ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
]

dwarves = [
    DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
    DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
]

print(feast_of_the_dwarves(dwarves))