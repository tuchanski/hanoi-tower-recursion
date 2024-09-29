from model import *

menu = Menu()
gameboard = Hanoi()

def default_hanoi_play():
    print(f"\n- Min. number of moves for 7 disks:", gameboard.min_moves(7))

def hanoi_play():
    try:
        disk_value = int(input("\n- Enter number of disks: "))
        print(f"- Min. number of moves for {disk_value} disks:", gameboard.min_moves(disk_value))
    except ValueError:
        print("\nError: Invalid input. Please enter a valid integer.")
    except RecursionError:
        print("Error: Please enter a valid number of disks.")

def main():
    while True:
        menu.show()
        mode = menu.selection()

        if mode == 1:
            hanoi_play()
        elif mode == 2:
            default_hanoi_play()
        elif mode == 0:
            print("\nProgram has been finished!")
            break
        else:
            print("\nThis isn't an option!\nValue must be in range 0-2.")
        
if __name__ == "__main__":
    main()
