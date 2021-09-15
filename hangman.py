import json
import random
words = []

# read json file
def read_json(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

# return colored string
def color_string(string, color):
    if color == "red":
        return "\033[31m" + string + "\033[0m"
    elif color == "green":
        return "\033[32m" + string + "\033[0m"
    elif color == "yellow":
        return "\033[33m" + string + "\033[0m"
    elif color == "blue":
        return "\033[34m" + string + "\033[0m"
    elif color == "magenta":
        return "\033[35m" + string + "\033[0m"
    elif color == "cyan":
        return "\033[36m" + string + "\033[0m"
    elif color == "white":
        return "\033[37m" + string + "\033[0m"
    else:
        return string

def random_item(list):
    return list[random.randint(0, len(list) - 1)]

# validate if string if char
def is_char(string):
    return string.isalpha() and len(string) == 1


def update_word(word, letter, index):
    return word[:index] + letter + word[index + 1:]

def start_game():
    # clear console
    print("\033[2J")
    word = random_item(words)
    ghost_word = "_" * len(word)
    chances = 7


    while True:
        if chances == 0:
            print(color_string("You lost! The word was: " + word, "magenta"))
            break
        print(color_string("You have " + str(chances) + " chances left", "cyan"))
        print(color_string(ghost_word, "green"))
        char = input(color_string("Guess a letter: ", "yellow"))
        if is_char(char):
            chances -= 1
            if char in word:
                print(color_string("Correct!", "green"))
                ghost_word = update_word(ghost_word, char, word.index(char))
            else:
                print(color_string("Wrong!", "red"))
        else:
            print(color_string("Please enter a valid character.", "red"))
        


def main():
    global words
    words = read_json("word-bank.json")
    while True:
        start_game()
        play = input(color_string("Do you want to play again? (y/n) ","red"))
        if play == "y":
            continue
        else:
            print(color_string("Bye!", "cyan"))
            break

main()