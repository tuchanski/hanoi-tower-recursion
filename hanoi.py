class Hanoi:

    def __init__(self) -> None:
        pass

    def game(self, n, first, second, third):

        # Caso base: Se não houver discos para mover, não faz nada.
        if n == 0:
            return 0
        # Move (n-1) discos da haste de origem para a haste auxiliar, usando a haste de destino como auxiliar.
        moves = self.game(n - 1, first, third, second)
        # Move (n-1) discos da haste auxiliar para a haste de destino, usando a haste de origem como auxiliar.
        moves += 1 + self.game(n - 1, second, first, third)
        return moves

    def min_moves(self, n):
        return self.game(n, 'A', 'B', 'C')
