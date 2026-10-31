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
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25.0, 30, 0.8)
    plant1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()
    print(f"Growth this week: {plant1.growth_rate * 7:.1f} cm")
