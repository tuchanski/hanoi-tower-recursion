class Menu:

    def __init__(self) -> None:
        pass

    def show(self):
        print("\n- Hanoi Tower -\n[1] - Min disks moves\n[2] - Default (7 disks)\n[0] - Exit")

    def select_mode(self):
        try:
            mode =  int(input("Choose here: "))
            return mode
        except ValueError:
            pass
