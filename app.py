from word import *

def main():
    print("[N]ew Game\n[E]xit\n[C]hoose Language")
    option = input("Option: ").upper()
    match option:
        case "N":
            new_game()
        case "E":
            exit()
        case "C":
            choose_language()
        case _:
            print("[Error] Invalid Option, please try again.\n")
            main()

                

if __name__ == '__main__':
    main()