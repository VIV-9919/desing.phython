import time
import sys

# Lyrics list with text, delay, and color codes
# Colors: Red, Yellow, Green, Cyan, Blue, Magenta, White
lyrics = [
    ("Jaaye Sajna Dhurandhar... 😭", 2, "\033[91m"),
    ("Nit Khaire Di Khushiyan...", 3, "\033[93m"),
    ("Ke Haath Vich Danda...", 3, "\033[92m"),
    ("Te Jeev Vich Chandiyan!", 4, "\033[96m"),
    ("Saada Kutta Kutta? Tuhaada Kutta Tommy...", 4, "\033[94m"),
    ("Saadi Boli Boli? Tuhaadi Boli Mummy...", 4, "\033[95m"),
    ("Dhiktana... Dhiktana...", 3, "\033[37m"),
    ("Dil Ke Tukde Tukde Ho Gaye Yaar! 💔", 5, "\033[91m")
]

print("\033[1mStarting Serial Hero Player (Line-by-Line Code)...\n\033[0m")

# Loop to print each line with a typewriter effect
for i, (line, delay, color) in enumerate(lyrics):
    # Print the line number and the crying emoji
    sys.stdout.write(f"{color}{i+1}. 💧 ")
    
    # Typewriter effect for the "Hero" feel
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.12)  # Dheere-dheere rone wala effect
    
    print("\033[0m")  # Reset color for next line
    time.sleep(delay)

print("\n\033[1;92mScript are ended Hero script! ✅\033[0m")