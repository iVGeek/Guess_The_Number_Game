import random
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class GameLevel:
    def __init__(self, name, min_value, max_value, max_attempts):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts

def play_game(player1, player2=None):
    if player2:
        print(Fore.CYAN + "Player 1: {}, Player 2: {}\n".format(player1, player2))
    else:
        print(Fore.CYAN + "Player: {}\n".format(player1))

    level = select_game_level()
    target_number = random.randint(level.min_value, level.max_value)
    guess_count = 0

    while True:
        if player2:
            current_player = player1 if guess_count % 2 == 0 else player2
            print(Fore.YELLOW + "Current Player: {}".format(current_player))
        else:
            current_player = player1
        guess = int(input(Fore.WHITE + "Guess a number between {} and {}: ".format(level.min_value, level.max_value)))
        guess_count += 1

        if guess < target_number:
            print(Fore.RED + "Too low!")
        elif guess > target_number:
            print(Fore.RED + "Too high!")
        else:
            print(Fore.GREEN + "Congratulations, {}! You guessed the number in {} tries!".format(current_player, guess_count))
            confetti_animation()
            play_again = input(Fore.YELLOW + "Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                play_game(player1, player2)
            else:
                print(Fore.CYAN + "Thank you for playing!")
                break

        if guess_count == level.max_attempts:
            print(Fore.RED + "Game over! The correct number was {}.".format(target_number))
            play_again = input(Fore.YELLOW + "Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                play_game(player1, player2)
            else:
                print(Fore.CYAN + "Thank you for playing!")
                break

def select_game_level():
    print(Fore.CYAN + "Select a game level:")
    print(Fore.YELLOW + "1. Easy (1-10, 6 attempts)")
    print(Fore.YELLOW + "2. Medium (1-50, 4 attempts)")
    print(Fore.YELLOW + "3. Hard (1-100, 3 attempts)")
    choice = input(Fore.WHITE + "Enter the level number: ")

    if choice == '1':
        return GameLevel("Easy", 1, 10, 6)
    elif choice == '2':
        return GameLevel("Medium", 1, 50, 4)
    elif choice == '3':
        return GameLevel("Hard", 1, 100, 3)
    else:
        print(Fore.RED + "Invalid choice. Defaulting to Medium level.")
        return GameLevel("Medium", 1, 50, 4)

# Confetti animation
def confetti_animation():
    confetti_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    for _ in range(10):
        confetti = ""
        for _ in range(10):
            confetti += random.choice(confetti_colors) + " * "
       

