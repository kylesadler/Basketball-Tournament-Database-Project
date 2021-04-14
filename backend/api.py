import sys

def add_game(home, away, court, date):
    print(f"adding game {home} {away} {court} {date} <br> <br>")



COMMAND_TO_FUNCTION = {
    'add_game': add_game,
}


if __name__ == '__main__':
    command = sys.argv[1]
    args = sys.argv[2:]   

    print(f"running {command} on arguments: {', '.join(args)} <br> <br>")

    # try:
    COMMAND_TO_FUNCTION[command](*args)
    # except:
        # pass

