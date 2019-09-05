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
        df['rain_game'] = df['rain_game'].astype(int)

        df.to_csv('matches_adding_rain_info.csv', index=False)

        df.to_sql('with_rain', conn, if_exists='append', index=False)

        #new_table_q = """ CREATE TABLE with_rain (Match_ID, Date, HomeTeam, AwayTeam, FTHG, FTAG, FTR, rain_game);"""
        #with open('matches_adding_rain_info.csv')
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
    
    def season_summary(self):
        """ This method generates a dataframe of the season summary for each team
        """

        q = """ SELECT HomeTeam as Club,
            (h_goals_for + a_goals_for) AS total_goals,
            (h_win + a_win) AS wins,
            (h_rain_win + h_rain_draw + h_rain_loss + a_rain_win + a_rain_draw + a_rain_loss) AS rain_games,
            (h_rain_win + a_rain_win) AS rain_wins
            
            FROM 
            
            (SELECT HomeTeam,
                SUM(CASE WHEN FTHG > FTAG THEN 1 ELSE 0 END) AS h_win,
                SUM(CASE WHEN FTHG = FTAG THEN 1 ELSE 0 END) AS h_draw,
                SUM(CASE WHEN FTHG < FTAG THEN 1 ELSE 0 END) AS h_loss,
                SUM(FTHG) AS h_goals_for,
                SUM(FTAG) AS h_goals_agst,
                SUM(CASE WHEN FTHG > FTAG AND rain_game = 1 THEN 1 ELSE 0 END) AS h_rain_win,
                SUM(CASE WHEN FTHG = FTAG AND rain_game = 1 THEN 1 ELSE 0 END) AS h_rain_draw,
                SUM(CASE WHEN FTHG < FTAG AND rain_game = 1 THEN 1 ELSE 0 END) AS h_rain_loss
                
                FROM with_rain
                
                GROUP BY HomeTeam
                ORDER BY HomeTeam)

            JOIN

            (SELECT AwayTeam,
                SUM(CASE WHEN FTAG > FTHG THEN 1 ELSE 0 END) AS a_win,
                SUM(CASE WHEN FTAG = FTHG THEN 1 ELSE 0 END) AS a_draw,
                SUM(CASE WHEN FTAG < FTHG THEN 1 ELSE 0 END) AS a_loss,
                SUM(FTAG) AS a_goals_for,
                SUM(FTHG) AS a_goals_agst,
                SUM(CASE WHEN FTAG > FTHG AND rain_game = 1 THEN 1 ELSE 0 END) AS a_rain_win,
                SUM(CASE WHEN FTAG = FTHG AND rain_game = 1 THEN 1 ELSE 0 END) AS a_rain_draw,
                SUM(CASE WHEN FTAG < FTHG AND rain_game = 1 THEN 1 ELSE 0 END) AS a_rain_loss            
            
                FROM with_rain
                
                GROUP BY AwayTeam
                ORDER BY AwayTeam)
            
            ON (HomeTeam == AwayTeam)
            
            ORDER BY total_goals DESC, wins DESC, rain_games DESC, rain_wins DESC;
            """
        c.execute(q)
        df = pd.DataFrame(c.fetchall())
        df.columns = [x[0] for x in c.description]
        df['rain_win_percent'] = (df['rain_wins'] / df['rain_games']) * 100
        df['rain_win_percent'] = df['rain_win_percent'].round(decimals=2)
        return df

        '''q = f"""SELECT HomeTeam as Club,
            (h_win + a_win + h_draw + a_draw + h_loss + a_loss) AS matches_played,
            (h_win + a_win) AS wins,
            (h_draw + a_draw) AS draws,
            (h_loss + a_loss) AS losses,
            (h_goals_for + a_goals_for) AS GF,
            (h_goals_agst + a_goals_agst) AS GA,
            (h_goals_for + a_goals_for - h_goals_agst - a_goals_agst) AS GD,
            ((h_win + a_win) * 3 + (h_draw + a_draw)) AS Pts

            FROM 
            
            (SELECT HomeTeam,
                SUM(CASE WHEN FTHG > FTAG THEN 1 ELSE 0 END) AS h_win,
                SUM(CASE WHEN FTHG = FTAG THEN 1 ELSE 0 END) AS h_draw,
                SUM(CASE WHEN FTHG < FTAG THEN 1 ELSE 0 END) AS h_loss,
                SUM(FTHG) AS h_goals_for,
                SUM(FTAG) AS h_goals_agst
            
            FROM Matches
            WHERE Season = 2011
            GROUP BY HomeTeam
            ORDER BY HomeTeam)

            JOIN

            (SELECT AwayTeam,
                SUM(CASE WHEN FTAG > FTHG THEN 1 ELSE 0 END) AS a_win,
                SUM(CASE WHEN FTAG = FTHG THEN 1 ELSE 0 END) AS a_draw,
                SUM(CASE WHEN FTAG < FTHG THEN 1 ELSE 0 END) AS a_loss,
                SUM(FTAG) AS a_goals_for,
                SUM(FTHG) AS a_goals_agst
            
            FROM Matches
            WHERE Season = 2011
            GROUP BY AwayTeam
            ORDER BY AwayTeam)
            
            ON (HomeTeam == AwayTeam)
            
            ORDER BY total_goals DESC, wins DESC;
            """'''
    
    @classmethod
    def team_names(self):
        """ This method generates a dataframe of all the team names"""
        q = """SELECT TeamName
            FROM Teams;
            """
        c.execute(q)
        df = pd.DataFrame(c.fetchall())
        df.columns = [x[0] for x in c.description]
        return df

test = QueryExecutor(team_name='test')
#test.create_rain_pd.head
#print(test.create_rain_pd())
#print(test.team_names())
print(test.season_summary())