import random
import os
from termcolor import colored
from pyfiglet import Figlet
from time import sleep
from pyfiglet import figlet_format
from operator import itemgetter
from datetime import datetime

MAX_LEADERBOARD_SIZE = 5
leaderboard = []

class GameLevel:
    def __init__(self, name, min_value, max_value, max_attempts, color):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts
        self.color = color

def display_welcome_screen():
    f = Figlet(font='big')
    print(colored(f.renderText("Guess the Number!"), "cyan"))
    print(colored("Welcome to Guess the Number!", "cyan"))
    print(colored("Game developed by iVGeek\n", "cyan"))
    print(colored("Initializing game...", "cyan"))
    print_animation()
    print(colored("Game ready!\n", "green"))

def print_animation():
    animation_frames = ["[■     ]", "[ ■    ]", "[  ■   ]", "[   ■  ]", "[    ■ ]", "[     ■]", "[    ■ ]", "[   ■  ]", "[  ■   ]", "[ ■    ]"]
    for frame in animation_frames:
        print(frame, end="\r")
        sleep(0.5)

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
            confetti = colored(figlet_format("Congratulations!", font="starwars"), "yellow")
            print(confetti)
            update_leaderboard(current_player, guess_count, level.name)
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

def update_leaderboard(player, score, level):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    leaderboard.append((player, score, level, date))
    leaderboard.sort(key=itemgetter(1))  # Sort leaderboard by score in ascending order
    if len(leaderboard) > MAX_LEADERBOARD_SIZE:
        leaderboard.pop(0)  # Remove the lowest score if leaderboard size exceeds the maximum


def display_leaderboard():
    if not leaderboard:
        print(colored("No leaderboard data available.", "red"))
        return

    print(colored("Leaderboard", "cyan"))
    print("---------------------------")
    
    # Sort the leaderboard in descending order based on the score
    sorted_leaderboard = sorted(leaderboard, key=itemgetter(1), reverse=True)

    for entry in sorted_leaderboard:
        player, score, level, date = entry
        if score == 0:
            score_text = "0 (Not on leaderboard)"
        else:
            score_text = str(score)
        print("Player: {}, Score: {}, Level: {}, Date: {}".format(player, score_text, level, date))
    
    # Check if there are players with a score of zero who are not on the leaderboard
    for player_score in leaderboard:
        if player_score[1] == 0:
            player_name = player_score[0]
            if any(entry[0] == player_name for entry in sorted_leaderboard):
                continue
            print("Player: {}, Score: 0 (Not on leaderboard)".format(player_name))

    print("---------------------------")



def clear_leaderboard():
    leaderboard.clear()
    print(colored("Leaderboard cleared.", "green"))

# Two-player mode
def play_two_players():
    print(colored("Two-Player Mode\n", "magenta"))
    player1 = input(colored("Enter Player 1 name: ", "blue"))
    player2 = input(colored("Enter Player 2 name: ", "blue"))
    print(colored("\nLet's begin!\n", "cyan"))
    play_game(player1, player2)

# Single-player mode against AI
def play_with_ai():
    print(colored("Single-Player Mode against AI\n", "magenta"))
    player1 = input(colored("Enter your name: ", "blue"))
    print(colored("\nLet's begin!\n", "cyan"))
    play_game(player1)

# Main menu
def main():
    display_welcome_screen()

    while True:
        print(colored("Main Menu", "cyan"))
        print("---------------------------")
        print(colored("1. Play Two Players", "green"))
        print(colored("2. Play with AI", "yellow"))
        print(colored("3. View Leaderboard", "blue"))
        print(colored("4. Clear Leaderboard", "red"))
        print(colored("5. Quit", "magenta"))
        print("---------------------------")

        choice = input(colored("Enter your choice: ", "blue"))

        if choice == '1':
            play_two_players()
        elif choice == '2':
            play_with_ai()
        elif choice == '3':
            display_leaderboard()
        elif choice == '4':
            clear_leaderboard()
        elif choice == '5':
            print(colored("Goodbye!", "cyan"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == '__main__':
    main()

