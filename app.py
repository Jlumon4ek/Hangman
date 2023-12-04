import os
import random


def main():
    print("[MENU] [N]ew Game or [E]xit")
    option = input("Option: ").upper()
    match option:
        case "N":
            new_game()
        case "E":
            exit()
        case _:
            print("Invalid Option")

def new_game():
    word = get_word()
    print(word)
    pass

def get_word():

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, 'resources', 'words.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        count_of_words = len(lines)
        word_index = random.randint(0, count_of_words - 1)
        word = lines[word_index].strip()

    return word


if __name__ == '__main__':
    main()