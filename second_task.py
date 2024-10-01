import random
from abc import ABC, abstractmethod


class BadGuy(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def action(self):
        ...


class Alien(BadGuy):
    def action(self):
        return "Aliens fly on round sausage around cows"


class Thanos(BadGuy):
    def action(self):
        return f"{self.name} trying to destroy Earth"


class Hero(ABC):
    def __init__(self, name, attacks):  # list
        self.name = name
        self.attacks = attacks

    @abstractmethod
    def attack(self):
        ...


class ChuckNorris(Hero):
    def __init__(self):
        super().__init__("Chuck Norris", ["PIU PIU", "SHAU SHAU"])

    def attack(self):
        return random.choice(self.attacks)


class City(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_random_bad_guy(self):
        ...


class NewYork(City):
    def __init__(self):
        super().__init__("New York")

    def get_random_bad_guy(self):
        return self._bad_guys_manager.get_random_bad_guy()

    def _create_bad_guys_manager(self):
        manager = BadGuysManager(self)
        manager.add_bad_guy(Thanos("Thanos"))
        manager.add_bad_guy(Alien("Aliens"))
        return manager

    def _initialize_bad_guys_manager(self):
        if not hasattr(self, "_bad_guys_manager"):
            self._bad_guys_manager = self._create_bad_guys_manager()

    def _get_bad_guys_manager(self):
        self._initialize_bad_guys_manager()
        return self._bad_guys_manager

    def __repr__(self):
        return f"<NewYork '{self.name}'>"


class BadGuysManager:
    def __init__(self, city):
        self._city = city
        self._bad_guys = []

    def add_bad_guy(self, bad_guy):
        self._bad_guys.append(bad_guy)

    def remove_bad_guy(self, bad_guy):
        if bad_guy in self._bad_guys:
            self._bad_guys.remove(bad_guy)

    def get_random_bad_guy(self):
        return random.choice(self._bad_guys)


class Media(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_message(self, message):
        ...


class TV(Media):
    def __init__(self):
        super().__init__("TV")

    def get_message(self, message):
        return f"Watch only on our channel! {message}"


class Newspaper(Media):
    def __init__(self):
        super().__init__("Newspaper")

    def get_message(self, message):
        return f"Only on our paper!! {message}"


def main(superhero, media, city):
    city._initialize_bad_guys_manager()

    bad_guy = city.get_random_bad_guy()

    action = bad_guy.action()  # описание что делает
    attack = superhero.attack()

    result = media.get_message(f"{action} \n{attack} \n{superhero.name} saved {city.name} from {bad_guy.name}")
    return result

superhero = ChuckNorris()
tv_media = TV()
new_york = NewYork()
print(main(superhero, tv_media, new_york))
