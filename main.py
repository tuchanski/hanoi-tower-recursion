from menu import Menu
from hanoi import Hanoi

def main():

    menu = Menu()
    hanoi = Hanoi()

    while True:
        menu.show()
        mode = menu.select_mode()
        try:
            if mode == 1:
                n = int(input("\n- Enter number of disks: "))
                print(f"- Min. number of moves for {n} disks:", hanoi.min_moves(n))
            elif mode == 2:
                print(f"\n- Min. number of moves for 7 disks:", hanoi.min_moves(7))
            elif mode == 0:
                print("\nProgram has been finished!")
                break
            else:
                print("\nError: Invalid input")
        except ValueError:
            print("\nError: Invalid input. Please enter a valid integer.")
        except RecursionError:
            print("Error: Please enter a valid number of disks.")

if __name__ == "__main__":
    main()
