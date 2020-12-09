# flexOptimizer2.0

The updated Version of this application is roster_generator.  Go to that repository instead.

THIS PROGRAM IS OLD AND DOESN'T RUN AS WELL AS roster_generator.



This is an application that creates fantasy football rosters based on loaded in csv files.  Load in a csv file with name players.csv and the header: player, price, position, floor, ceiling:

- player is a string that is the name of the player
- price is an int that is the price of the player
- position is an enum (string) that depending on the position is either: QB, RB, WR, TE, DF
- floor is an int that is the floor prediction of points for the player
- ceiling is an int that is the ceiling prediciton of points for the player

There are currently three csv files- players_small.csv, players_medium.csv, players_large.csv files.  They are the same and can create over 100000 rosters depending on the parameters.  Replace any of the files with one of the same name to see unique data and use the prompts to run the appropriate one (the last question is which file should be used- small, medium or large).

The output allows for up to three csv files with all of the potential roster combinations as well as a column for "amount left for flex."  This is one of the parameters set at the start of running the program through a prompt.

At the start of the program a prompt appears to set the minimum and maximum of the amount left for the flex, as well as the budget.  There is a prompt to allow for multiple csv files but they all currently point to three identical files.  To get a large number of rosters, set the minimum flex amount at 2600, the maximum flex amount at 9000 and the budget for 50000.  Currently all three size files are the same so selecting small, medium or large does not matter.
