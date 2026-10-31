class Plant:

    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate
        self._stat_count = self.Stats()

    @staticmethod
    def is_year_old(x: int) -> bool:
        if x >= 365:
            return True
        else:
            return False

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0, 0)

    def display(self) -> None:
        print(
            f"Stats: {self._stat_count._grow_count}"
            + f" grow, {self._stat_count._age_count} ", end="")
        print(f"age, {self._stat_count._show_count} show")

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._stat_count._show_count += 1

    def grow(self) -> None:
        self._height += self._growth_rate
        self._stat_count._grow_count += 1

    def age(self, inc: int) -> None:
        self._age += inc
        self._stat_count._age_count += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height > 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age > 0:
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")


class Flower(Plant):

    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float, color: str) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloom is False:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):

    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_count = 0

    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float, diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self._diameter = diameter

    def display(self) -> None:
        super().display()
        print(f" {self._stat_count._shade_count} shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._diameter}cm wide.")
        self._stat_count._shade_count += 1


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        harvest_season: str,
        nutritional_value: float
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {round(self._nutritional_value)}")

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float, color: str) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42


def display_stats(plant: Plant) -> None:
    plant.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year_old(400)}")
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8, "red")
    rose.show()
    print(f"[statistics for {rose._name}]")
    display_stats(rose)
    print(f"[asking the {rose._name.lower()} top grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    print(f"[statistics for {rose._name}]")
    display_stats(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 2, 5.0)
    oak.show()
    print(f"[statistics for {oak._name}]")
    display_stats(oak)
    print(f"[asking the {oak._name.lower()} to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak._name}]")
    display_stats(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, 30, "yellow")
    sunflower.show()
    print(f"[make {sunflower._name.lower()} grow, age and bloom]")
    sunflower.age(20)
    sunflower.grow()
    sunflower.bloom()
    sunflower.show()
    print(f"[statistics for {sunflower._name}]")
    display_stats(sunflower)
    print("")
    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    print(f"[statistics for {anonymous._name}]")
    display_stats(anonymous)
