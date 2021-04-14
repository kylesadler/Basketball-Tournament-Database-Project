import sys
from sql_database import SQLDatabase

""" NOTE: returns a string. May be html """

# SQLDatabase

def add_game(home, away, court, date):
    print(f"adding game {home} {away} {court} {date} <br> <br>")

def add_team(name, mascot, seed):
    print(f"adding team {name} {mascot} as {seed} seed <br> <br>")

def add_result(game, home, away):
    print(f"adding result {game} {home} {away} <br> <br>")

def view_teams(game, home, away):
    print(f"viewing teams <br> <br>")





COMMAND_TO_FUNCTION = {
    'add_game': add_game,
    'add_team': add_team,
    'add_result': add_result,
}


if __name__ == '__main__':
    command = sys.argv[1]
    args = sys.argv[2:]   

    # print(f"running {command} on arguments: {', '.join(args)} <br> <br>")

    try:
        COMMAND_TO_FUNCTION[command](*args)
    except TypeError:
        print("ERROR")
        print("incorrect number of arguments\n")
        raise
    except Exception as e:
        print("ERROR")
        print(str(e))
        raise

