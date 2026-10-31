class Plant:

    def __init__(self, name: str, height: int,
                 age: int, growth_rate: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1

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

    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float, diameter: float) -> None:
        super().__init__(name, height, age, growth_rate)
        self._diameter = diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self._diameter}cm wide.")


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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, 0.8, "red")
    rose.show()
    print(f"[asking the {rose._name.lower()} to bloom]")
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 2, 5.0)
    oak.show()
    print(f"[asking the {oak._name.lower()} to produce shade]")
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, 2.1, "April", 0)
    tomato.show()
    print(f"[make {tomato._name.lower()} grow and age for 20 days]")
    for i in range(0, 20):
        tomato.grow()
        tomato.age()
    tomato.show()
