import sys
from sql_database import SQLDatabase
# from util import *
import util

""" NOTE: return a list of objects. May be html strings """

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
    # util.send(f"adding game {home} {away} {court} {date} <br> <br>")

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
                    SUPPLIER.COUNTRY = 'USA'
                    AND INVENTORY_MGMT.ITEM_ID = ITEM.ID
                    AND INVENTORY_MGMT.SUPPLIER_ID = SUPPLIER.ID;'''
    

    return database.select(query)

def add_team(name, mascot, seed):
    return f"adding team {name} {mascot} as {seed} seed <br> <br>"

def add_result(game, home, away):
    return f"adding result {game} {home} {away} <br> <br>"

def get_teams():
    query = f'''SELECT 
            ID, NAME, MASCOT, TOURNAMENT_SEED
        FROM TEAM;'''

    return database.select(query)


def get_team_name_mascot_id():
    query = f'''SELECT 
        NAME, MASCOT, ID
    FROM TEAM;'''

    return database.select(query)


def get_results_by_team_id(id):
    
    query = f'''SELECT 
            TEAM.NAME,
            GAME.HOME_TEAM_ID AS HOME,
            GAME.AWAY_TEAM_ID AS AWAY,
            GAME.COURT_NUM AS CourtNumber,
            GAME.DATE AS Date,
            RESULT.HOME_TEAM_SCORE AS HomeScore,
            RESULT.AWAY_TEAM_SCORE AS AwayScore
        FROM TEAM
        INNER JOIN GAME
        INNER JOIN RESULT
        WHERE
            TEAM.ID = '{util.clean_input(id)}'
            AND (GAME.AWAY_TEAM_ID = TEAM.ID OR GAME.HOME_TEAM_ID = TEAM.ID),
            AND RESULT.GAME_ID = GAME.ID;'''

    return database.select(query)





COMMAND_TO_FUNCTION = {
    'add_game': add_game,
    'add_team': add_team,
    'add_result': add_result,
    'get_teams': get_teams,
}




if __name__ == '__main__':
    command = sys.argv[1]
    args = sys.argv[2:]   

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

