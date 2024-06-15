from gameboard import *
def main():

    menu = Menu()
    gameboard = Hanoi()

    while True:

        menu.show()
        mode = menu.selection()

        try:
            if mode == 1:
                disk_value = int(input("\n- Enter number of disks: "))
                print(f"- Min. number of moves for {disk_value} disks:", gameboard.min_moves(disk_value))
            elif mode == 2:
                print(f"\n- Min. number of moves for 7 disks:", gameboard.min_moves(7))
            elif mode == 0:
                print("\nProgram has been finished!")
                break
            else:
                print("\nThis isn't an option!\nValue must be in range 0-2.")
        except ValueError:
            print("\nError: Invalid input. Please enter a valid integer.")
        except RecursionError:
            print("Error: Please enter a valid number of disks.")

if __name__ == "__main__":
    main()
