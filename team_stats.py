import pandas as pd
import numpy as np
import sqlite3
from Query_Executor import QueryExecutor as qe

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

class team_stats():
    """ This class contains methods needed to build out data tables for each team
    """

    def __init__(self):
        pass

    def table_build(self):
        df = pd.read_csv('matches_adding_rain_info.csv')
        
        for team in qe.team_names()['TeamName']:
            for match in df:
                rain_total = 0
                if ((team == match['HomeTeam'] | team == match['AwayTeam']) & match['rain_game']):
                    rain_total += 1
                else:
                    continue
                print(team, rain_total)
    

test = team_stats()
test.table_build()