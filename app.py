import os
import random


def main():
    print("[Menu] [N]ew Game or [E]xit")
    option = input("Option: ").upper()
    match option:
        case "N":
            new_game()
        case "E":
            exit()
        case _:
            print("[Error] Invalid Option, please try again.\n")
            main()

def new_game():
    word = get_word()
    guessed_letters = []
    
    print(f"[Word]: {'*' * len(word)}, {word}")
    
    count_of_wrong_letters = 0

    while count_of_wrong_letters < 8:
        letter = input("Letter: ")
        match letter:
            case letter if letter in word:
                guessed_letters.append(letter)
                print("[Congratulations] You found a letter!")
                encrypted_word = ''.join([letter if letter in guessed_letters else '*' for letter in word])
                print(f"[Word]: {encrypted_word}")

                if encrypted_word == word:
                    print("\n[Congratulations] You win!\n")
                    main()
                    
            case letter if letter not in word:
                print("[Error] Wrong letter")
                count_of_wrong_letters += 1

    if count_of_wrong_letters == 8:
        print("\n[Game Over] You lose!\n")
        main()
    

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