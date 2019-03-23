# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# / Title: Flex Optimizer                                                                                             /
# / Author: Adam Noor                                                                                                 /
# / Date Created: December 7, 2018                                                                                    /
# /                                                                                                                   /
# / Description: This program takes in a players.csv file containing fantasy football players, prices,                /
# / positions, floor and ceiling and creates a rosters.csv file with every viable roster that contains                /
# / a set amount remaining for the flex position.                                                                     /
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Libraries
import time
import csv
from itertools import combinations


# Player Object
class Player:
    def __init__(self, name, price, position, floor, ceiling):
        self.name = name
        self.price = price
        self.position = position
        self.floor = floor
        self.ceiling = ceiling


# Global Lists, Dictionaries and Variables
players = []
quarter_backs = []
running_backs = []
wide_receivers = []
tight_ends = []
defenses = []
rb_combos = []
wr_combos = []
rb_wr_combos = []
rb_wr_qb_combos = []
rb_wr_qb_te_combos = []
full_roster = []
roster_breakdown = {}
players_csv = ''     # This variable holds the name of the file that is exported
rosters_csv = ''     # This variable holds the name of the file that is exported
roster_budget = 50000  # This variable sets the total budget for the roster
flex_min = 2600    # This variable sets the minimum amount that can be left for the flex
flex_max = 9300     # This variable sets the maximum amount that can be left for the flex
iterations = 10000     # This variable sets how often progress is shown in the console as the program runs


# Functions

def get_user_information():

    global flex_min
    flex_min = int(input("What is the minimum amount for the flex? "))
    global flex_max
    flex_max = int(input("What is the maximum amount for the flex? "))
    while flex_max < flex_min:
        print("The maximum must be more than " + str(flex_min))
        flex_max = int(input("What is the maximum amount for the flex? "))
    global roster_budget
    roster_budget = int(input("What is the budget? "))
    while flex_max > roster_budget:
        print("The budget must be more than " + str(roster_budget))
        roster_budget = int(input("What is the budget? "))
    choice = int(input("Which roster size (small- 1, medium- 2, large- 3 or other number)? "))
    global players_csv
    global rosters_csv

    if choice == 1:
        players_csv = 'players_small.csv'
        rosters_csv = 'rosters_small.csv'

    elif choice == 2:
        players_csv = 'players_medium.csv'
        rosters_csv = 'rosters_medium.csv'

    else:
        players_csv = 'players_large.csv'
        rosters_csv = 'rosters_large.csv'

    print("Your min flex is: ", flex_min)
    print("Your max flex is: ", flex_max)
    print("Your budget is: ", roster_budget)


def open_csv():
    with open(players_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)  # this functions avoids the header being the first object of the list

        for line in csv_reader:
            player: Player = Player(line[0], line[1], line[2], line[3], line[4])

            if not players:
                players.insert(0, player)
                roster_breakdown[player.name] = 0
            else:
                players.append(player)
                roster_breakdown[player.name] = 0


def set_players():

    for player in players:
        if player.position == "QB":
            if not quarter_backs:
                quarter_backs.insert(0, player)
            else:
                quarter_backs.append(player)
        elif player.position == "RB":
            if not running_backs:
                running_backs.insert(0, player)
            else:
                running_backs.append(player)
        elif player.position == "WR":
            if not wide_receivers:
                wide_receivers.insert(0, player)
            else:
                wide_receivers.append(player)
        elif player.position == "TE":
            if not tight_ends:
                tight_ends.insert(0, player)
            else:
                tight_ends.append(player)
        elif player.position == "DF":
            if not defenses:
                defenses.insert(0, player)
            else:
                defenses.append(player)


def set_running_backs():
    combo = combinations(running_backs, 2)
    for p in list(combo):

        if not rb_combos:
            rb_combos.insert(0, p)
        else:
            rb_combos.append(p)


def set_wide_receivers():
    combo = combinations(wide_receivers, 3)
    for p in list(combo):
        if not wr_combos:
            wr_combos.insert(0, p)
        else:
            wr_combos.append(p)
    print("Done 1 of 5.  The number of players is " + str(len(players)))


def combine_wr_rb():
    p = -1
    while p < len(rb_combos) - 1:
        p += 1
        q = 0
        while q < len(wr_combos):
            current_array = [rb_combos[p][0], rb_combos[p][1], wr_combos[q][0], wr_combos[q][1], wr_combos[q][2]]
            if not rb_wr_combos:
                rb_wr_combos.insert(0, current_array)
            else:
                rb_wr_combos.append(current_array)
            q += 1
    print("Done 2 of 5.  The number of RB/WR combos is " + str(len(rb_wr_combos)))


def combine_wr_rb_qb():
    p = -1
    while p < len(quarter_backs) - 1:
        p += 1
        q = 0
        while q < len(rb_wr_combos):
            current_array = [quarter_backs[p], rb_wr_combos[q][0], rb_wr_combos[q][1], rb_wr_combos[q][2],
                             rb_wr_combos[q][3], rb_wr_combos[q][4]]
            if not rb_wr_qb_combos:
                rb_wr_qb_combos.insert(0, current_array)
            else:
                rb_wr_qb_combos.append(current_array)
            q += 1
    print("Done 3 of 5.  The number of RB/WR/QB combos is " + str(len(rb_wr_qb_combos)))


def combine_wr_rb__qb_te():
    p = -1
    while p < len(tight_ends) - 1:
        p += 1
        q = 0
        while q < len(rb_wr_qb_combos):
            current_array = [tight_ends[p], rb_wr_qb_combos[q][0], rb_wr_qb_combos[q][1],
                             rb_wr_qb_combos[q][2], rb_wr_qb_combos[q][3],
                             rb_wr_qb_combos[q][4], rb_wr_qb_combos[q][5]]
            if not rb_wr_qb_te_combos:
                rb_wr_qb_te_combos.insert(0, current_array)
            else:
                rb_wr_qb_te_combos.append(current_array)
            q += 1
    print("Done 4 of 5.  The number of RB/WR/QB/TE combos is " + str(len(rb_wr_qb_te_combos)))


def complete_roster():
    total_combos = len(defenses) * len(rb_wr_qb_te_combos)
    print("Running 5 of 5.  This could take some time.  The total number of combinations is " +
          str(total_combos))
    p = -1
    count = 0
    with open(rosters_csv, 'w') as f:
        the_writer = csv.writer(f)
        the_writer.writerow(['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'WR3', 'TE', 'DF', 'FX', 'Floor', 'Ceiling'])
    while p < len(defenses) - 1:
        p += 1
        q = 0
        while q < len(rb_wr_qb_te_combos):
            qb = rb_wr_qb_te_combos[q][1]
            rb1 = rb_wr_qb_te_combos[q][2]
            rb2 = rb_wr_qb_te_combos[q][3]
            wr1 = rb_wr_qb_te_combos[q][4]
            wr2 = rb_wr_qb_te_combos[q][5]
            wr3 = rb_wr_qb_te_combos[q][6]
            te = rb_wr_qb_te_combos[q][0]
            df = defenses[p]
            price = int(qb.price) + int(rb1.price) + int(rb2.price) + int(wr1.price) + int(wr2.price) + int(wr3.price)\
                + int(te.price) + int(df.price)
            floor = int(qb.floor) + int(rb1.floor) + int(rb2.floor) + int(wr1.floor) + int(wr2.floor) + int(wr3.floor)\
                + int(te.floor) + int(df.floor)
            ceiling = int(qb.ceiling) + int(rb1.ceiling) + int(rb2.ceiling) + int(wr1.ceiling) + int(wr2.ceiling)\
                + int(wr3.ceiling) + int(te.ceiling) + int(df.ceiling)

            flex_amount = roster_budget - price
            count += 1
            current_array = [qb, rb1, rb2, wr1, wr2, wr3, te, df]
            if flex_min <= flex_amount <= flex_max:
                if not full_roster:
                    full_roster.insert(0, [current_array, flex_amount])
                else:
                    full_roster.append([current_array, flex_amount])
                for player in current_array:
                    roster_breakdown[str(player.name)] += 1
                with open(rosters_csv, 'a') as f:
                    the_writer = csv.writer(f)
                    current_write_array = []
                    for player in current_array:
                        if not current_write_array:
                            current_write_array.insert(0, str(player.name))
                        else:
                            current_write_array.append(str(player.name))
                    current_write_array.append(int(flex_amount))
                    current_write_array.append(int(floor))
                    current_write_array.append(int(ceiling))

                    the_writer.writerow(current_write_array)
            q += 1
            if count % iterations == iterations / 2:
                print("Completed valid rosters: " + str(len(full_roster)) + "   Total Iterations: " + str(count))
    count = 0
    print("Done 5 of 5.  Complete with no errors. The total number of valid rosters is " + str(len(full_roster)) +
          "(" + str(round(100 * float(len(full_roster)) / float(total_combos))) + "%)")
    for key in roster_breakdown:
        valid_roster_percent = str(round(100 * float(roster_breakdown[key]) / float(len(full_roster)), 2))
        no_rosters_with_player = roster_breakdown[key]
        print(str(no_rosters_with_player) + " rosters have " + key + " (" + valid_roster_percent + "%)")
        count += 1


def run_program():
    get_user_information()
    start = time.process_time()
    print("Timer Started")
    open_csv()
    set_players()
    set_running_backs()
    set_wide_receivers()
    combine_wr_rb()
    combine_wr_rb_qb()
    combine_wr_rb__qb_te()
    complete_roster()
    end = time.process_time()
    print("Time (in seconds): " + str(end-start))
    # print(end - start)


# Function Call to Start Program
run_program()
