import sys
from sql_database import SQLDatabase
# from util import *
import util

""" 

arguments cleaned and passed to functions automatically
NOTE: return a list of objects. May be html strings

"""

MYSQL_USER = 'krs028'
MYSQL_PASS ='PhoV9bi2'
database = SQLDatabase('localhost', MYSQL_USER, MYSQL_PASS, MYSQL_USER)


""" 

        query = f'''SELECT 
                        SUPPLIER.ID AS SUPPLIER_ID,
                        SUPPLIER.NAME AS SUPPLIER_NAME,
                        SUPPLIER.PHONE_NUMBER AS SUPPLIER_PHONE_NUMBER,
                        ITEM.NAME AS COFFEE_NAME,
                        ITEM.ROASTING_TYPE
                    FROM INVENTORY_MGMT
                    INNER JOIN ITEM
                    INNER JOIN SUPPLIER
                    WHERE
                        SUPPLIER.COUNTRY = '{clean_input(country)}'
                        AND INVENTORY_MGMT.ITEM_ID = ITEM.ID
                        AND INVENTORY_MGMT.SUPPLIER_ID = SUPPLIER.ID;'''
        

        headers, rows = self.database.select(query)






        supplier_id = self.generate_unique_id('SUPPLIER')
        self.database.insert('SUPPLIER', f"{supplier_id},'{name}',{number},'{country}'")

        self.database.insert('INVENTORY_MGMT', f"{item_id},{supplier_id},0,0")


        # print new supplier and other suppliers with same item
        print("New supplier created.")
        print_table(*self.database.select(f"SELECT * FROM SUPPLIER WHERE ID = {supplier_id};"))

        print("\nOther suppliers that provide the same item:")
        print_table(*self.database.select(
            f'''SELECT
                SUPPLIER.NAME
            FROM INVENTORY_MGMT
            INNER JOIN SUPPLIER
            WHERE
                SUPPLIER.ID = INVENTORY_MGMT.SUPPLIER_ID
                AND INVENTORY_MGMT.ITEM_ID = {item_id}
                AND INVENTORY_MGMT.SUPPLIER_ID != {supplier_id};'''
        ))



        self.database.update(
            f'''Update INVENTORY_MGMT
            SET TOTAL_AVAILABLE = {new_available}
            WHERE ITEM_ID = {item_id};'''
            )

"""


def add_game(home, away, court, date):
    _id = database.generate_unique_id('GAME')
    database.insert('GAME', f"{_id},{court},{home},{away},STR_TO_DATE('{date}','%m/%d/%Y')")

def add_team(name, mascot, seed):

    _id = database.generate_unique_id('TEAM')
    database.insert('TEAM', f"{_id},'{name}','{mascot}',{seed}")


def add_result(game, home, away):
    _id = database.generate_unique_id('RESULT')
    database.insert('RESULT', f"{_id},{game},{home},{away}")


def add_player(name, position, team_id):
    _id = database.generate_unique_id('PLAYER')
    database.insert('PLAYER', f"{_id},'{name}','{position}',{team_id}")


def get_teams():
    return database.select('SELECT * FROM TEAM;')


def get_results():
    return database.select('SELECT * FROM RESULT;')

def get_games():
    return database.select('SELECT * FROM GAME;')

def get_games_and_results():
    return database.select(
        f'''SELECT
            GAME.HOME_TEAM_ID AS HOME_ID,
            (SELECT TEAM.NAME FROM TEAM WHERE TEAM.ID = GAME.HOME_TEAM_ID) AS HOME_NAME,
            (SELECT TEAM.MASCOT FROM TEAM WHERE TEAM.ID = GAME.HOME_TEAM_ID) AS HOME_MASCOT,
            RESULT.HOME_TEAM_SCORE AS HOME_SCORE,
            GAME.AWAY_TEAM_ID AS AWAY_ID,
            (SELECT TEAM.NAME FROM TEAM WHERE TEAM.ID = GAME.AWAY_TEAM_ID) AS AWAY_NAME,
            (SELECT TEAM.MASCOT FROM TEAM WHERE TEAM.ID = GAME.AWAY_TEAM_ID) AS AWAY_MASCOT,
            RESULT.AWAY_TEAM_SCORE AS AWAY_SCORE,
            GAME.COURT_NUM AS COURT_NUMBER,
            GAME.DATE AS DATE
        FROM GAME
        LEFT JOIN RESULT
            ON GAME.ID = RESULT.GAME_ID;'''
        )

def get_players():
    return database.select(
        '''SELECT 
            PLAYER.NAME AS NAME,
            PLAYER.POSITION AS POSITION,
            CONCAT(TEAM.NAME, ' ', TEAM.MASCOT) AS TEAM
        FROM PLAYER
        INNER JOIN TEAM
            WHERE PLAYER.TEAM_ID = TEAM.ID;'''
        )

def get_roster():
    return database.select('SELECT * FROM PLAYER;')


def get_team_name_mascot_id():
    query = f'''SELECT 
        NAME, MASCOT, ID
    FROM TEAM;'''

    return database.select(query)


def get_results_by_team_id(_id):
    
    query = f'''SELECT
                GAME.HOME_TEAM_ID AS HOME_ID,
                (SELECT TEAM.NAME FROM TEAM WHERE TEAM.ID = GAME.HOME_TEAM_ID) AS HOME_NAME,
                (SELECT TEAM.MASCOT FROM TEAM WHERE TEAM.ID = GAME.HOME_TEAM_ID) AS HOME_MASCOT,
                RESULT.HOME_TEAM_SCORE AS HOME_SCORE,
                GAME.AWAY_TEAM_ID AS AWAY_ID,
                (SELECT TEAM.NAME FROM TEAM WHERE TEAM.ID = GAME.AWAY_TEAM_ID) AS AWAY_NAME,
                (SELECT TEAM.MASCOT FROM TEAM WHERE TEAM.ID = GAME.AWAY_TEAM_ID) AS AWAY_MASCOT,
                RESULT.AWAY_TEAM_SCORE AS AWAY_SCORE,
                GAME.COURT_NUM AS COURT_NUMBER,
                GAME.DATE AS DATE
            FROM TEAM
            INNER JOIN GAME
            INNER JOIN RESULT
            WHERE
                TEAM.ID = '{_id}'
                AND (GAME.AWAY_TEAM_ID = TEAM.ID OR GAME.HOME_TEAM_ID = TEAM.ID)
                AND RESULT.GAME_ID = GAME.ID;'''

    return database.select(query)


def get_results_by_date(date):
    query = f'''SELECT
                GAME.HOME_TEAM_ID AS HOME_ID,
                (SELECT TEAM.NAME FROM TEAM WHERE TEAM.ID = GAME.HOME_TEAM_ID) AS HOME_NAME,
                (SELECT TEAM.MASCOT FROM TEAM WHERE TEAM.ID = GAME.HOME_TEAM_ID) AS HOME_MASCOT,
                RESULT.HOME_TEAM_SCORE AS HOME_SCORE,
                GAME.AWAY_TEAM_ID AS AWAY_ID,
                (SELECT TEAM.NAME FROM TEAM WHERE TEAM.ID = GAME.AWAY_TEAM_ID) AS AWAY_NAME,
                (SELECT TEAM.MASCOT FROM TEAM WHERE TEAM.ID = GAME.AWAY_TEAM_ID) AS AWAY_MASCOT,
                RESULT.AWAY_TEAM_SCORE AS AWAY_SCORE,
                GAME.COURT_NUM AS COURT_NUMBER,
                GAME.DATE AS DATE
            FROM TEAM
            INNER JOIN GAME
            INNER JOIN RESULT
            WHERE
                GAME.DATE = STR_TO_DATE('{date}','%m/%d/%Y')
                AND (GAME.AWAY_TEAM_ID = TEAM.ID OR GAME.HOME_TEAM_ID = TEAM.ID)
                AND RESULT.GAME_ID = GAME.ID;'''

    print(query)
    return database.select(query)


def get_roster_by_team(_id):
    return database.select(
        f'''SELECT 
            PLAYER.NAME AS NAME,
            PLAYER.POSITION AS POSITION,
            CONCAT(TEAM.NAME, ' ', TEAM.MASCOT) AS TEAM
        FROM PLAYER
        INNER JOIN TEAM
            WHERE PLAYER.TEAM_ID = TEAM.ID
            AND TEAM.ID = '{_id}';'''
        )



COMMAND_TO_FUNCTION = {
    'add_game': add_game,
    'add_team': add_team,
    'add_result': add_result,
    'add_player': add_player,

    'get_teams': get_teams,
    'get_players': get_players,
    'get_roster': get_roster,
    'get_games': get_games,
    'get_results': get_results,

    'get_games_and_results': get_games_and_results,
    'get_team_name_mascot_id': get_team_name_mascot_id,
    'get_results_by_team_id': get_results_by_team_id,
    'get_results_by_date': get_results_by_date,
    'get_roster_by_team': get_roster_by_team,
}




if __name__ == '__main__':
    command = sys.argv[1]
    args = [util.clean_input(x) for x in sys.argv[2:]]

    # print(f"running {command} on arguments: {', '.join(args)} <br> <br>")

    try:
        output = COMMAND_TO_FUNCTION[command](*args)
        util.send(output)
    except TypeError:
        print("ERROR")
        print("incorrect number of arguments\n")
        raise
    except Exception as e:
        print("ERROR")
        print(str(e))
        raise

