# Font colors:
class fcolors:
    PINK = '\033[95m'
    BLUE = '\033[96m'
    GREY = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Background colors:
class bcolors:
    BLACK = "\u001b[40m"
    RED = "\u001b[41m"
    GREEN = "\u001b[42m"
    YELLOW = "\u001b[43m"
    BLUE = "\u001b[44m"
    MAGENTA = "\u001b[45m"
    CYAN = "\u001b[46m"
    WHITE = "\u001b[47m"


if __name__ == "__main__":
    print(fcolors.RED+"Error: This module is not meant to be excecuted!!!"+fcolors.RESET)
    exit(1)
