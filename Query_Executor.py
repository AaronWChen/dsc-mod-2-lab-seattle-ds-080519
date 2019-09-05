import pandas as pd
import sqlite3
import numpy as np
from WeatherGetter import WeatherGetter as wg

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

class QueryExecutor():
    """ This class contains methods needed to query the provided soccer database.
    """

    def __init__(self, team_name):
        self.team_name = team_name

    def find_rain_dates(self):
        """ The number of games is too large to access the API in one day. This method was
        run in a Jupyter Notebook file, but it takes the original list of game dates from 
        the 2011 season, extracts the unique dates, uses those smaller list of dates for 
        the API calls, creates a column in a dataframe with a boolean for rain game,
        and exports that dataframe as a csv so that the API does not need to be called.
        """

        q = """SELECT Match_ID, Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR
                FROM Matches
                WHERE Season = 2011;
            """
        
        c.execute(q)
        df = pd.DataFrame(c.fetchall())
        df.columns = [x[0] for x in c.description]

        unique_dates = pd.DataFrame(df['Date'].unique(), columns=['Date'])
        unique_dates['rain_game'] = unique_dates.apply(lambda x: wg.get_weather(x['Date']), axis=1)

        rain_dates = unique_dates[unique_dates['rain_game'] == True]
        df['rain_game'] = df['Date'].isin(rain_dates['Date'])

        df.to_csv('matches_adding_rain_info.csv')

    """def create_rain_pd(self):
       '''This was the original method used to call the Dark Sky API to return the rain
        status of a game day. However, this resulted in too many API calls and was modified
        into the method above
        '''
        q = '''SELECT Match_ID, Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR
                FROM Matches
                WHERE Season = 2011;
            '''
        c.execute(q)
        df = pd.DataFrame(c.fetchall())
        df.columns = [x[0] for x in c.description]

        df['Date']
        df['rain_game'] = df.apply(lambda x: wg.get_weather(x['Date']), axis=1)
        print(df.head())
        print(wg.get_weather('2011-11-01'))
        return df[:30]
        pass"""


        
    
    # def get_each_team(self):
    #     team_name = self.team_name

    #     q = f"""SELECT HomeTeam as Club,
    #         (h_win + a_win + h_draw + a_draw + h_loss + a_loss) AS matches_played,
    #         (h_win + a_win) AS wins,
    #         (h_draw + a_draw) AS draws,
    #         (h_loss + a_loss) AS losses,
    #         (h_goals_for + a_goals_for) AS GF,
    #         (h_goals_agst + a_goals_agst) AS GA,

    #         FROM 
            
    #         (SELECT HomeTeam,
    #             SUM(CASE WHEN FTHG > FTAG THEN 1 ELSE 0 END) AS h_win,
    #             SUM(CASE WHEN FTHG = FTAG THEN 1 ELSE 0 END) AS h_draw,
    #             SUM(CASE WHEN FTHG < FTAG THEN 1 ELSE 0 END) AS h_loss,
    #             SUM(FTHG) AS h_goals_for,
    #             SUM(FTAG) AS g_goals_agst
            
    #         FROM Matches
    #         WHERE Season = 2011
    #         GROUP BY HomeTeam
    #         ORDER BY HomeTeam)

    #         JOIN

    #         (SELECT AwayTeam,
    #             SUM(CASE WHEN FTAG > FTHG THEN 1 ELSE 0 END) AS h_win,
    #             SUM(CASE WHEN FTAG = FTHG THEN 1 ELSE 0 END) AS h_draw,
    #             SUM(FTHG) AS h_goals_for,
    #             SUM(FTAG) AS g_goals_agst
            
    #         FROM Matches
    #         WHERE Season = 2011
    #         GROUP BY HomeTeam
    #         ORDER BY HomeTeam)
    #         Matches
    #         WHERE (Season = 2011 AND (HomeTeam))

    #         """
    
test = QueryExecutor(team_name='test')
#test.create_rain_pd.head
print(test.create_rain_pd())