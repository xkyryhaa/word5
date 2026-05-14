import os
import random
from colorama import *
from pyfiglet import figlet_format
from tabulate import tabulate

init()
base_words_file = "C:\\my_education\\word5\\data\\len5"
print(figlet_format("Worldle"))


def random_word(path = base_words_file) -> str:
    words = []
    with open(path,"r",encoding="utf-8") as file:
        for line in file:
            words.append(line.strip())

    result = random.choice(words)

    return result


def start_game(word):
    MAX_ATTEMPTS = 6
    TotalAttempts = 0
    game_res = False
    res_word = list(word)

    while TotalAttempts < MAX_ATTEMPTS and not game_res:

        temp = ["_"] * 5

        data = list(input(f"{Fore.LIGHTBLUE_EX}\nВведите слово из 5 букв:\n").lower())

        if len(data) != 5:
            print(Fore.RED + "Введите слово из 5 букв!")
            continue

        if data == res_word:
            print(Fore.GREEN + "Поздравляю, вы угадали слово!")

            next_game = input(
                "Хочешь сыграть новую игру?\n1. Да\n2. Нет\n"
            )

            if next_game == "1":
                return start_game(random_word())
            else:
                return "Спасибо за игру!"

        for i in range(5):
            if data[i] == res_word[i]:
                temp[i] = data[i].upper()

        for letter in temp:
            if letter == "_":
                print(Fore.MAGENTA + letter, end=" ")
            else:
                print(Fore.GREEN + letter, end=" ")

        print()

        TotalAttempts += 1

    print(Fore.RED + f"\nИгра окончена! Слово было: {word.upper()}")
start_game(random_word())


