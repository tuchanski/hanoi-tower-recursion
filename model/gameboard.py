class Hanoi:
    def __init__(self) -> None:
        pass

    def min_moves(self, n: int) -> int:
        if n < 0:
            raise ValueError("Number of disks cannot be negative")
        elif n == 1:
            return 1
        else:
            return 2 * self.min_moves(n - 1) + 1

class Menu:
    def __init__(self) -> None:
        pass

    def show(self):
        print("\n- Hanoi Tower | Min. Moves Calculator -\n[1] - Custom value\n[2] - Default (7 disks)\n[0] - Exit")

    def selection(self):
        try:
            mode =  int(input("Choose here: "))
            return mode
        except ValueError:
            pass
