import random
from termcolor import colored
from pyfiglet import figlet_format

class GameLevel:
    def __init__(self, name, min_value, max_value, max_attempts, color):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts
        self.color = color

def play_game(player1, player2=None):
    if player2:
        print("Player 1: {}, Player 2: {}\n".format(player1, player2))
    else:
        print("Player: {}\n".format(player1))

    level = select_game_level()
    target_number = random.randint(level.min_value, level.max_value)
    guess_count = 0
    attempts_left = level.max_attempts

    while True:
        if player2:
            current_player = player1 if guess_count % 2 == 0 else player2
            print("Current Player: {}".format(current_player))
        else:
            current_player = player1
        guess = int(input(colored("Guess a number between {} and {}: ".format(level.min_value, level.max_value), "blue")))
        guess_count += 1
        attempts_left -= 1

        if guess < target_number:
            print(colored("Too low!", "red"))
        elif guess > target_number:
            print(colored("Too high!", "red"))
        else:
            print(colored("Congratulations, {}! You guessed the number in {} tries!".format(current_player, guess_count), "green"))
            # Add confetti using pyfiglet
            confetti = colored(figlet_format("Congratulations!", font="starwars"), "yellow")
            print(confetti)
            break

        if attempts_left == 0:
            print(colored("Game over! The correct number was {}.".format(target_number), "red"))
            break

    play_again = input(colored("Do you want to play again? (y/n): ", "blue"))
    if play_again.lower() == 'y':
        if player2:
            play_game(player1, player2)
        else:
            play_game(player1)
    else:
        print(colored("Thank you for playing!", "cyan"))

def select_game_level():
    print("Select a game level:")
    print(colored("1. Easy (1-10, 8 attempts)", "green"))
    print(colored("2. Medium (1-50, 6 attempts)", "yellow"))
    print(colored("3. Hard (1-100, 4 attempts)", "red"))
    choice = input(colored("Enter the level number: ", "blue"))

    if choice == '1':
        return GameLevel("Easy", 1, 10, 8, "green")
    elif choice == '2':
        return GameLevel("Medium", 1, 50, 6, "yellow")
    elif choice == '3':
        return GameLevel("Hard", 1, 100, 4, "red")
    else:
        print(colored("Invalid choice. Defaulting to Medium level.", "red"))
        return GameLevel("Medium", 1, 50, 4, "yellow")

# Two-player mode
def play_two_players():
    print(colored("Two-Player Mode\n", "cyan"))
    player1 = input(colored("Enter Player 1 name: ", "blue"))
    player2 = input(colored("Enter Player 2 name: ", "blue"))
    print(colored("\nLet's begin!\n", "cyan"))
    play_game(player1, player2)

# Single-player mode against AI
def play_with_ai():
    print(colored("Single-Player Mode against AI\n", "cyan"))
    player1 = input(colored("Enter your name: ", "blue"))
    print(colored("\nLet's begin!\n", "cyan"))
    play_game(player1)

# Main menu
def main():
    print(colored("Welcome to Guess the Number!\n", "cyan"))
    print(colored("1. Two-Player Mode", "magenta"))
    print(colored("2. Single-Player Mode against AI", "magenta"))
    choice = input(colored("Enter your choice (1 or 2): ", "blue"))

    if choice == '1':
        play_two_players()
    elif choice == '2':
        play_with_ai()
    else:
        print(colored("Invalid choice. Please try again.", "red"))

if __name__ == '__main__':
    main()

