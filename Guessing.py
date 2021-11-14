import random
import sys


def welcome():
    print("Welcome to the game the aim is to guess the right number? ")
    print("The number will between 1 and 100")
    print("You only have 5 tries")


def game_over():
    guess = int(input("If yes press 1: "))
    if guess == 1:
        game()
    else:
        sys.exit()


def game():
    turn = 1
    n = random.randint(1, 100)
    guess = int(input())
    while guess != n:
        if turn <= 4:
            if 1 < guess > 100:
                guess = int(input("Guess between 1 and 100 "))
            elif guess > n:
                guess = int(input("Guess lower "))
            elif guess < n:
                guess = int(input("Guess higher "))
            turn += 1
        else:
            print("Game Over, would you like to play again?")
            game_over()
    else:
        print("Congratulation would you like to play again")
        game_over()


welcome()
game()
