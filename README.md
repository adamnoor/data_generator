# flexOptimizer2.0

This is an application that creates fantasy football rosters based on loaded in csv files.  Load in a csv file with name players.csv and the header: player, price, position, floor, ceiling

player is a string that is the name of the player/
price is an int that is the price of the player/
position is a string that depending on the position is either: QB, RB, WR, TE, DF/
floor is an int that is the floor prediction of points for the player/
ceiling is an int that is the ceiling prediciton of points for the player/

There is currently a players.csv file that creates over 100000 rosters.  Replace the file with one of the same name to see unique data.  Later versions will accomodate multiple csv files.

The output is a csv file with all of the potential roster combinations as well as a column for "amount left for flex."  This is one of the parameters set at the start of running the program through a prompt.

At the start of the program a prompt appears to set the minimum and maximum of the amount left for the flex, as well as the budget.  There is a prompt to allow for multiple csv files but they all currently point to the same file.  The get_user_info function where the update to allow for multiple csv files will happen. 
