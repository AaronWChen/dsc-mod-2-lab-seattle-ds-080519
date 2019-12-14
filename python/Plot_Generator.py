import pandas as pd
import sqlite3
import numpy as np
from WeatherGetter import WeatherGetter as wg
import matplotlib.pyplot as plt

class Plot_Generator():
    df = pd.read_csv('data/2011_summary.csv')

    f, ax = plt.subplots(1, figsize=(10,5))
    bar_width = 1
    bar_l = [i for i in range(len(df['Club']))]
    tick_pos = [i + (bar_width/15) for i in bar_l]

    p1 = ax.bar(bar_l, df['wins'], label='Wins', alpha=0.9, color='#019600',
            width=bar_width, edgecolor='white')

    p2 = ax.bar(bar_l, df['draws'], bottom=df['wins'], label='Draws',
            alpha=0.9, color='#3C5F5A',width=bar_width,edgecolor='white')

    p3 = ax.bar(bar_l,df['losses'],bottom=df['wins'] + df['draws'], label='Losses',
            alpha=0.9, color='#219AD8', width=bar_width, edgecolor='white')

    plt.xticks(tick_pos, df['Club'])
    ax.set_ylabel("Match Results")
    ax.set_xlabel("Clubs")

    plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
    plt.ylim(0,40)
    ax.legend([p1, p2, p3], ['Wins', 'Draws', 'Losses'])
    ax.set_title(f'2011 Soccer Season Summary')

    plt.setp(plt.gca().get_xticklabels(),rotation=45,horizontalalignment='right')
    plt.savefig('plots/2011_season_wins_draws_losses_summary.png')
    

    ################################################


    f, ax = plt.subplots(1, figsize=(10,5))
    bar_width = 1
    bar_l = [i for i in range(len(df['Club']))]
    tick_pos = [i + (bar_width/15) for i in bar_l]

    p1 = ax.bar(bar_l, df['rain_win_percent'], label='Wins', alpha=0.9, color='#219AD8',
            width=bar_width, edgecolor='white')

    plt.xticks(tick_pos, df['Club'])
    ax.set_ylabel("Winning Percentage in Rain")
    ax.set_xlabel("Clubs")

    plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
    plt.ylim(0,105)

    ax.set_title(f'Rain Match Win Percentage for Clubs During 2011 Season')

    plt.setp(plt.gca().get_xticklabels(),rotation=45,horizontalalignment='right')
    plt.savefig('plots/2011_season_rain_win_percentage_summary.png')
    

    ################################################
    

    df2 = pd.read_csv('data/2011_summary.csv', index_col='Club',usecols=['Club','wins','draws','losses'])
    for club in df['Club']:
        f, ax = plt.subplots(1, figsize=(10,5))
        bar_width = 1
        bar_l = [0,1,2]
        tick_pos = [i + (bar_width/2) for i in bar_l]
        p1 = ax.bar(0, 
                    df2.loc[club]['wins'], 
                    label='Wins', 
                    alpha=0.9, 
                    color='#019600',
                    width=bar_width, 
                    edgecolor='white')
        p2 = ax.bar(1, 
                    df2.loc[club]['draws'], 
                    label='Draws', 
                    alpha=0.9, 
                    color='#3C5F5A',
                    width=bar_width, 
                    edgecolor='white')
        p3 = ax.bar(2, 
                    df2.loc[club]['losses'], 
                    label='Losses', 
                    alpha=0.9, 
                    color='#219AD8',
                    width=bar_width, 
                    edgecolor='white')
        ax.set_ylabel("Match Results")
        ax.set_xlabel(club)
        plt.ylim(0,40)
        ax.legend([p1, p2, p3], ['Wins', 'Draws', 'Losses'])
        ax.set_title(f'2011 Season Summary for {club}')
        ax.set_xticklabels(['','',''])
        plt.tick_params(
                        axis='x',          # changes apply to the x-axis
                        which='both',      # both major and minor ticks are affected
                        bottom=False,      # ticks along the bottom edge are off
                        top=False
                        )
        plt.savefig(f'plots/2011_season_summary_{club}.png')
    pass

