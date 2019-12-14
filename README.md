
# Kickin in the Rain: The Impact of Rain Upon Soccer Wins
### Author: Aaron Washington Chen
### GitHub Profile [Here](https://github.com/AaronWChen)

## Executive Summary

This repo uses a given sqlite database and an API to hybridize data to visualize how much of an effect rain has on a soccer league's win/tie/loss percentages.

In short, the impact is inconlusive; while the top 2 most successful teams in this league in this season did win more rain games than they lost, there are teams in the upper middle and even one team in the lower rankings which have 100% rain win rates but these wins did not propel them to the upper tier.

This is likely due to a small sample size: Few games were played in the rain, so the overall effect of winning a small amount of rain games would wash out over the 32 game season.

The emphasis for teams should not be to prepare to dominate games in poor weather conditions and they should focus on improving overall play instead.

![Overall Season Results for Each Team in the 2011 Season](https://github.com/AaronWChen/Kickin-in-the-Rain/blob/master/plots/2011_season_wins_draws_losses_summary.png)

![Rain Win Percentage for Each Team in the 2011 Season](https://github.com/AaronWChen/Kickin-in-the-Rain/blob/master/plots/2011_season_rain_win_percentage_summary.png)


## Project Information

This project uses 2011 soccer season data from this [kaggle page](https://www.kaggle.com/laudanum/footballdelphi). The goal was to extract, transform, and load (ETL) the given SQL database and combine the information with weather data from the [DarkSky API](https://darksky.net/dev) with API calls. 

The goal was to display the number of wins, ties, and losses for each team and compare that information to each team's corresponding win percentage in the rain to see how much of an effect rain wins contributed to the overall season results.


## Improvements and Next Steps
The original sqlite file has a lot of information that can be used! It is possible to play with the information more; perhaps showing goals and goal differentials for each team over the course of the season. In addition, this relatively simple and well structured information can be converted over to a NoSQL type of database like MongoDB for experimentation.

The current implementation of weather only checks for a simple boolean of whether or not it rained on that game day in Berlin. However, not all of the games were played in Berlin and were played at different times. Future improvements can factor in the proper geography and meterology.


## Running the Code
If you are looking to run and/or work on this project yourself, you will need to 
1. Create an account with DarkSky to obtain an API key with them
2. Create a folder inside the repo root called secrets, and store the DarkSky API key in a dictionary inside a json file named "dark_sky_api.json". The key should be "key" and the value should be the API code.
3. Install Python 3 (I prefer and recommend Anaconda)
4. Clone [this repo](https://github.com/AaronWChen/Kickin-in-the-Rain)
5. Install the packages in the requirements.txt file via pip (pip install -r requirements.txt from command line)

If you want to see the high level execution and results of the code, you can navigate to the python/ directory of this repo, open a Jupyter server there, and explore the notebooks (particularly plotter.ipynb).

If you are looking to make changes to the code, I recommend using Visual Studio Code to open the files and edit.
