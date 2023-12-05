import os
import random
from app import main
from hangman_drawler import *

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'resources', 'en_wordlist.txt')


def choose_language():
    global file_path
    lang = input('Choose language: en - English, ru - Russian: ').lower()
    match lang:
        case 'en':
            file_path = os.path.join(current_directory, 'resources', 'en_wordlist.txt')
            main()
        case 'ru':
            file_path = os.path.join(current_directory, 'resources', 'ru_wordlist.txt')
            main()
    
    
def get_word():
    with open(file_path, 'r', encoding='utf-8') as file:        
        lines = file.readlines()
        count_of_words = len(lines)
        word_index = random.randint(0, count_of_words - 1)
        word = lines[word_index].strip()

    return word

def new_game():
    word = get_word()    
    guessed_letters = []
    count_of_wrong_letters = 0
    print(draw_hangman(count_of_wrong_letters))
    print(f"[Word]: {'*' * len(word)}")
       

    while count_of_wrong_letters <= 6:
        letter = input("Letter: ")
        match letter:
            case letter if letter in guessed_letters:
                print("[Error] This letter has already been entered, please try again.")

            case letter if not letter.isalpha() or len(letter) != 1:
                print("[Error] Invalid letter, please try again.")

            case letter if letter in word:
                guessed_letters.append(letter)
                print("[Congratulations] You found a letter!")
                encrypted_word = ''.join([letter if letter in guessed_letters else '*' for letter in word])
                print(f"[Word]: {encrypted_word}")

                if encrypted_word == word:
                    print("\n[Congratulations] You win!\n")
                    main()

            case letter if letter not in word:
                count_of_wrong_letters += 1
                guessed_letters.append(letter)
                
                print("[Error] Wrong letter")
                print(draw_hangman(count_of_wrong_letters))

                if count_of_wrong_letters == 6:
                    print(f"\n[Game Over] You lose! Word is {word}\n ")
                    main()

