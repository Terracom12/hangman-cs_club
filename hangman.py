import os
import time
import random
import screen


def generate_word():
    with open("wordlist.txt") as f:
        lines = f.readlines()
        return random.choice(lines)


def parseInput(letters_tried):
    valid = False
    letter = input("What letter would you like to guess: ").lower()
    while not valid:
        if len(letter) > 1 or len(letter) == 0:
            letter = input("Input must be a single character, try again: ")
            continue
        if letter in letters_tried:
            letter = input("You have already guessed \'" + letter + "\' try again: ")
            continue
        valid = True
    return letter


def checkInput(user_input, word, word_state):
    correct = False
    for i, c in enumerate(word):
        if user_input == c:
            correct = True
            word_state[i] = c
    return correct


def gameEnd(lives, word):
    if lives == 0:
        print(f"Unlucky you ran out of lives, the word was \'{word}\'")
    else:
        print(f"You guessed the word \'{word}\', congrats")


def gameLoop():
    lives = 6
    letters_tried = list()
    word = generate_word()
    word_state = ['_'] * (len(word) - 1)
    while lives > 0:
        screen.drawUI(word_state, lives, letters_tried)
        user_input = parseInput(letters_tried)
        letters_tried.append(user_input)
        if not checkInput(user_input, word, word_state):
            lives -= 1

        if '_' not in word_state:
            break

    screen.drawUI(word_state, lives, letters_tried)
    gameEnd(lives, word)

def main():
    gameLoop()


if __name__ == "__main__":
    main()
