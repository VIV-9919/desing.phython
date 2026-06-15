# Color codes for terminal output
class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

def chal_chal_re_bandeya():
    # Lyrics mapped with specific colors
    lyrics_with_colors = [
        (Colors.CYAN, "Tu khud ki khoj mein nikal..."),
        (Colors.YELLOW, "Tu kis liye hataash hai?"),
        (Colors.GREEN, "Tu chal tere wajood ki samay ko bhi talaash hai."),
        (Colors.RED, "Samay ko bhi talaash hai!"),
        (Colors.PURPLE, "---"),
        (Colors.CYAN, "Jo tujh se lipti bediyan, samajh na inko vastra tu,"),
        (Colors.YELLOW, "Yeh bediyan pighaal ke, bana le inko shastra tu."),
        (Colors.GREEN, "Bana le inko shastra tu!"),
        (Colors.RED, "---"),
        (Colors.PURPLE, "Charitra jab pavitra hai, toh kyun hai yeh dasha teri?"),
        (Colors.CYAN, "Yeh paapiyon ko haq nahi, ke lein pariksha teri."),
        (Colors.YELLOW, "Ke lein pariksha teri!")
    ]

    print(f"{Colors.BOLD}--- Playing: CHAL CHAL RE BANDEYA ---{Colors.END}\n")

    for color, line in lyrics_with_colors:
        if line == "---":
            print(f"{color}------------------------------------{Colors.END}")
        else:
            print(f"{color}🎵 {line}{Colors.END}")

# Run the song
chal_chal_re_bandeya()