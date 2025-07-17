import time
import math
import random
import os

# Terminal colors (ANSI escape codes)
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]
RESET = "\033[0m"

# ASCII art banner
def print_banner():
    banner = r"""
   ____                 _           _     
  / ___| ___   ___   __| | ___  ___| |__  
 | |  _ / _ \ / _ \ / _` |/ _ \/ __| '_ \ 
 | |_| | (_) | (_) | (_| |  __/\__ \ | | |
  \____|\___/ \___/ \__,_|\___||___/_| |_|

        🧪 Sandbox Terminal Tester 🧪
    """
    print(random.choice(colors) + banner + RESET)

# Progress bar
def progress_bar(task="Running", length=30):
    print(f"\n{task} Progress:")
    for i in range(length + 1):
        filled = "#" * i
        empty = " " * (length - i)
        percent = int((i / length) * 100)
        print(f"\r[{filled}{empty}] {percent}%", end="")
        time.sleep(0.05)
    print()

# Math animation
def spinning_cos_wave():
    print("\n🎢 Cosine Wave Animation:")
    for i in range(60):
        value = math.cos(i / 5) * 10
        indent = " " * (int(value) + 20)
        print(indent + "*")
        time.sleep(0.03)

# File writing test
def write_test_file():
    filename = "sandbox_output.txt"
    with open(filename, "w") as f:
        f.write("✅ Sandbox terminal file output works!\n")
        f.write("Random lucky number: " + str(random.randint(1000, 9999)) + "\n")
    print(f"\n📁 File '{filename}' created.")

# Terminal effects
def print_colored_messages():
    print("\n🎨 Color Output Test:")
    for color in colors:
        print(color + "Hello from the sandbox terminal!" + RESET)
        time.sleep(0.1)

def main():
    os.system("clear" if os.name == "posix" else "cls")
    print_banner()
    progress_bar("Testing Terminal")
    spinning_cos_wave()
    print_colored_messages()
    write_test_file()
    print("\n✅ All tests complete! 🎉")

if __name__ == "__main__":
    main()
