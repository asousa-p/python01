class Plant:

    def __init__(self, name: str, height: float,
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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    plant1: Plant = Plant("Rose", 15.0, 10, 0.8)
    plant1.show()
    print("")
    plant1.set_height(25)
    plant1.set_age(30)
    print("")
    plant1.set_height(-42)
    plant1.set_age(-42)
    print("")
    print("Current state:", end=" ")
    plant1.show()
