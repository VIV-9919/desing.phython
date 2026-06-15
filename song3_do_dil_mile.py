import time
import sys

# Lyrics list: (Line, Delay after line, Color Code)
# Colors: Red, Yellow, Green, Cyan, Blue, Magenta, White
lyrics = [
    ("🎶 (Soft Guitar Strumming...) 🎶", 4, "\033[97m"),
    ("Do dil mil rahe hain...", 4, "\033[91m"),
    ("Magar chupke chupke...", 4, "\033[93m"),
    ("Do dil mil rahe hain...", 4, "\033[92m"),
    ("Magar chupke chupke...", 4, "\033[96m"),
    ("Sabko ho rahi hai...", 3, "\033[94m"),
    ("Khabar chupke chupke...", 4, "\033[95m"),
    ("Do dil mil rahe hain...", 3, "\033[91m"),
    ("Magar chupke chupke... 🌹", 4, "\033[93m"),
    ("🎶 (Interlude) 🎶", 3, "\033[97m"),
    ("Saanson mein badi bechaini hai,", 4, "\033[92m"),
    ("Aankhon mein kai armaan hain...", 4, "\033[96m"),
    ("Khwabon mein kisi ka chehra hai,", 4, "\033[94m"),
    ("Honthon pe kisi ka naam hai...", 4, "\033[95m"),
    ("Is baat ka nazaara...", 3, "\033[91m"),
    ("Idhar chupke chupke...", 3, "\033[93m"),
    ("Udhar chupke chupke...", 4, "\033[92m"),
    ("Do dil mil rahe hain...", 3, "\033[96m"),
    ("Magar chupke chupke... 😭", 5, "\033[91m"),
    ("🎶 (Final Fade Out...) 🎶", 6, "\033[97m")
]

def hero_style_player():
    print("\033[1m🎤 Romantic Hero Player: 'Do Dil Mil Rahe Hain' 🎤\n\033[0m")
    time.sleep(1)

    for i, (line, delay, color) in enumerate(lyrics):
        # Line number and Heart/Drop effect
        sys.stdout.write(f"{color}{i+1:02d}. ❤️  ")
        
        # Typewriter effect (Emotional/Slow)
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.12) # Yeh wahi slow 'Ro-Ro kar' bolne wala speed hai
        
        print("\033[0m") # Reset color
        time.sleep(delay) # Waiting for the song rhythm

    print("\n\033[1;92mPura gaana khatam! Dil mil gaye. ✅\033[0m")

if __name__ == "__main__":
    try:
        hero_style_player()
    except KeyboardInterrupt:
        print("\n\033[91mGaana beech mein hi rok diya yaar! 💔\033[0m")