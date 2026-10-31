class Plant:

    def __init__(self, name: str, height: float,
                 age: int, growth_rate: float) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 3),
        Plant("Cactus", 5.0, 90, 0.1),
        Plant("Sunflower", 80.0, 45, 1),
        Plant("Fern", 15.0, 120, 0.3),
    ]

    for plant in plants:
        print("Created: ", end="")
        plant.show()
