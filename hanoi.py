class Hanoi:

    def __init__(self) -> None:
        pass

    def min_moves(self, n: int) -> int:
        if n < 0:
            raise ValueError("Number of disks cannot be negative")
        elif n == 1:
            return 1
        else:
            # Fórmula -> T(n) = 2n − 1
            return 2 * self.min_moves(n - 1) + 1
