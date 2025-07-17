import random
import time
import os

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    banner = r"""
   _____                      _             
  |  __ \                    | |            
  | |  \/_   _  ___  ___ ___ | | ___  _ __  
  | | __| | | |/ _ \/ __/ _ \| |/ _ \| '_ \ 
  | |_\ \ |_| |  __/ (_| (_) | | (_) | | | |
   \____/\__,_|\___|\___\___/|_|\___/|_| |_|                                                
    """
    print(YELLOW + banner + RESET)
    print(CYAN + "     🎲 Welcome to the Guessing Game! 🎲\n" + RESET)


def countdown(seconds=3):
    print(YELLOW + "Get ready..." + RESET)
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Go!\n")


def play_game():
    number = random.randint(1, 20)
    attempts = 5
    score = 0

    while attempts > 0:
        try:
            guess = int(input(f"🔢 Guess the number (1-20): "))
        except ValueError:
            print(RED + "❌ Please enter a valid number." + RESET)
            continue

        if guess == number:
            print(GREEN + "🎉 Correct! You guessed it!" + RESET)
            score += 1
            break
        elif guess < number:
            print(CYAN + "📉 Too low!" + RESET)
        else:
            print(CYAN + "📈 Too high!" + RESET)

        attempts -= 1
        print(f"💡 Attempts left: {attempts}\n")

    if attempts == 0:
        print(RED + f"😢 Out of attempts! The number was {number}.\n" + RESET)

    return score


def main():
    clear()
    print_banner()
    countdown()

    total_score = 0
    round_number = 1

    while True:
        print(f"\n🕹️ Round {round_number}")
        total_score += play_game()

        again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if again != 'y':
            break
        round_number += 1
        clear()
        print_banner()

    print(GREEN + f"\n🏁 Game Over! Your total score: {total_score} 🎯" + RESET)


if __name__ == "__main__":
    main()
