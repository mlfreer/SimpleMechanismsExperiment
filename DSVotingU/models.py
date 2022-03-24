from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
import decimal

author = 'Mikhail Freer'

doc = """
The code for the Dominant Strategy Voting Treatment with Unequal Strategy Space (DSxU treatment)
"""


class Constants(BaseConstants):
    name_in_url = 'DSVotingU'
    players_per_group = 4

    num_rounds = 10 # number of periods to be set to 10

    type_probability = .5 # probability of type of 2 and 3 being (a)


    # number of profiles:
    num_profiles = 24

    # defining the vector of preferences:
    preferences = [[[0 for x in range(0,6)] for x in range(0,6)] for x in range(0,24)]

# type (1):
    preferences[0][0] = [20, 15, 5, 0] # player 1
    preferences[0][1] = [5, 20, 15, 0] # player 2a
    preferences[0][2] = [15, 20, 5, 0] # player 2b
    preferences[0][3] = [5, 20, 15, 0] # player 3a
    preferences[0][4] = [15, 20, 5, 0] # player 3b
    preferences[0][5] = [5, 15, 20, 0] # player 4

# type (2):
    preferences[1][0] = [20, 0, 15, 5] # player 1
    preferences[1][1] = [5, 0, 20, 15] # player 2a
    preferences[1][2] = [15, 0, 20, 5] # player 2b
    preferences[1][3] = [5, 0, 20, 15] # player 3a
    preferences[1][4] = [15, 0, 20, 5] # player 3b
    preferences[1][5] = [5, 0, 15, 20] # player 4

# type (3):
    preferences[2][0] = [20, 5, 15, 0] # player 1
    preferences[2][1] = [5, 15, 20, 0] # player 2a
    preferences[2][2] = [15, 5, 20, 0] # player 2b
    preferences[2][3] = [5, 15, 20, 0] # player 3a
    preferences[2][4] = [15, 5, 20, 0] # player 3b
    preferences[2][5] = [5, 20, 15, 0] # player 4

# type (4):
    preferences[3][0] = [20, 0, 5, 15] # player 1
    preferences[3][1] = [5, 0, 15, 20] # player 2a
    preferences[3][2] = [15, 0, 5, 20] # player 2b
    preferences[3][3] = [5, 0, 15, 20] # player 3a
    preferences[3][4] = [15, 0, 5, 20] # player 3b
    preferences[3][5] = [5, 0, 20, 15] # player 4

# type (5):
    preferences[4][0] = [20, 15, 0, 5] # player 1
    preferences[4][1] = [5, 20, 0, 15] # player 2a
    preferences[4][2] = [15, 20, 0, 5] # player 2b
    preferences[4][3] = [5, 20, 0, 15] # player 3a
    preferences[4][4] = [15, 20, 0, 5] # player 3b
    preferences[4][5] = [5, 15, 0, 20] # player 4

# type (6):
    preferences[5][0] = [20, 5, 0, 15] # player 1
    preferences[5][1] = [5, 15, 0, 20] # player 2a
    preferences[5][2] = [15, 5, 0, 20] # player 2b
    preferences[5][3] = [5, 15, 0, 20] # player 3a
    preferences[5][4] = [15, 5, 0, 20] # player 3b
    preferences[5][5] = [5, 20, 0, 15] # player 4



# type (7):
    preferences[6][0] = [0, 20, 15, 5] # player 1
    preferences[6][1] = [0, 5, 20, 15] # player 2a
    preferences[6][2] = [0, 15, 20, 5] # player 2b
    preferences[6][3] = [0, 5, 20, 15] # player 3a
    preferences[6][4] = [0, 15, 20, 5] # player 3b
    preferences[6][5] = [0, 5, 15, 20] # player 4

# type (8):
    preferences[7][0] = [0, 5, 20, 15] # player 1
    preferences[7][1] = [0, 15, 5, 20] # player 2a
    preferences[7][2] = [0, 5, 15, 20] # player 2b
    preferences[7][3] = [0, 15, 5, 20] # player 3a
    preferences[7][4] = [0, 5, 15, 20] # player 3b
    preferences[7][5] = [0, 20, 5, 15] # player 4

# type (9):
    preferences[8][0] = [0, 5, 15, 20] # player 1
    preferences[8][1] = [0, 15, 20, 5] # player 2a
    preferences[8][2] = [0, 5, 20, 15] # player 2b
    preferences[8][3] = [0, 15, 20, 5] # player 3a
    preferences[8][4] = [0, 5, 20, 15] # player 3b
    preferences[8][5] = [0, 20, 15, 5] # player 4

# type (10):
    preferences[9][0] = [0, 15, 20, 5] # player 1
    preferences[9][1] = [0, 20, 5, 15] # player 2a
    preferences[9][2] = [0, 20, 15, 5] # player 2b
    preferences[9][3] = [0, 20, 5, 15] # player 3a
    preferences[9][4] = [0, 20, 15, 5] # player 3b
    preferences[9][5] = [0, 15, 5, 20] # player 4

# type (11):
    preferences[10][0] = [0, 15, 5, 20] # player 1
    preferences[10][1] = [0, 20, 15, 5] # player 2a
    preferences[10][2] = [0, 20, 5, 15] # player 2b
    preferences[10][3] = [0, 20, 15, 5] # player 3a
    preferences[10][4] = [0, 20, 5, 15] # player 3b
    preferences[10][5] = [0, 15, 20, 5] # player 4

# type (12):
    preferences[11][0] = [0, 20, 5, 15] # player 1
    preferences[11][1] = [0, 5, 15, 20] # player 2a
    preferences[11][2] = [0, 15, 5, 20] # player 2b
    preferences[11][3] = [0, 5, 15, 20] # player 3a
    preferences[11][4] = [0, 15, 5, 20] # player 3b
    preferences[11][5] = [0, 5, 20, 15] # player 4




# type (13):
    preferences[12][0] = [15, 20, 5, 0] # player 1
    preferences[12][1] = [20, 5, 15, 0] # player 2a
    preferences[12][2] = [20, 15, 5, 0] # player 2b
    preferences[12][3] = [20, 5, 15, 0] # player 3a
    preferences[12][4] = [20, 15, 5, 0] # player 3b
    preferences[12][5] = [15, 5, 20, 0] # player 4

# type (14):
    preferences[13][0] = [15, 5, 20, 0] # player 1
    preferences[13][1] = [20, 15, 5, 0] # player 2a
    preferences[13][2] = [20, 5, 15, 0] # player 2b
    preferences[13][3] = [20, 15, 5, 0] # player 3a
    preferences[13][4] = [20, 5, 15, 0] # player 3b
    preferences[13][5] = [15, 20, 5, 0] # player 4

# type (15):
    preferences[14][0] = [15, 5, 0, 20] # player 1
    preferences[14][1] = [20, 15, 0, 5] # player 2a
    preferences[14][2] = [20, 5, 0, 15] # player 2b
    preferences[14][3] = [20, 15, 0, 5] # player 3a
    preferences[14][4] = [20, 5, 0, 15] # player 3b
    preferences[14][5] = [15, 20, 0, 5] # player 4

# type (16):
    preferences[15][0] = [15, 0, 20, 5] # player 1
    preferences[15][1] = [20, 0, 5, 15] # player 2a
    preferences[15][2] = [20, 0, 15, 5] # player 2b
    preferences[15][3] = [20, 0, 5, 15] # player 3a
    preferences[15][4] = [20, 0, 15, 5] # player 3b
    preferences[15][5] = [15, 0, 5, 20] # player 4

# type (17):
    preferences[16][0] = [15, 0, 5, 20] # player 1
    preferences[16][1] = [20, 0, 15, 5] # player 2a
    preferences[16][2] = [20, 0, 5, 15] # player 2b
    preferences[16][3] = [20, 0, 15, 5] # player 3a
    preferences[16][4] = [20, 0, 5, 15] # player 3b
    preferences[16][5] = [15, 0, 20, 5] # player 4

# type (18):
    preferences[17][0] = [15, 20, 0, 5] # player 1
    preferences[17][1] = [20, 5, 0, 15] # player 2a
    preferences[17][2] = [20, 15, 0, 5] # player 2b
    preferences[17][3] = [20, 5, 0, 15] # player 3a
    preferences[17][4] = [20, 15, 0, 5] # player 3b
    preferences[17][5] = [15, 5, 0, 20] # player 4




# type (19):
    preferences[18][0] = [5, 20, 15, 0] # player 1
    preferences[18][1] = [15, 5, 20, 0] # player 2a
    preferences[18][2] = [5, 15, 20, 0] # player 2b
    preferences[18][3] = [15, 5, 20, 0] # player 3a
    preferences[18][4] = [5, 15, 20, 0] # player 3b
    preferences[18][5] = [20, 5, 15, 0] # player 4

# type (20):
    preferences[19][0] = [5, 20, 0, 15] # player 1
    preferences[19][1] = [15, 5, 0, 20] # player 2a
    preferences[19][2] = [5, 15, 0, 20] # player 2b
    preferences[19][3] = [15, 5, 0, 20] # player 3a
    preferences[19][4] = [5, 15, 0, 20] # player 3b
    preferences[19][5] = [20, 5, 0, 15] # player 4

# type (21):
    preferences[20][0] = [5, 0, 20, 15] # player 1
    preferences[20][1] = [15, 0, 5, 20] # player 2a
    preferences[20][2] = [5, 0, 15, 20] # player 2b
    preferences[20][3] = [15, 0, 5, 20] # player 3a
    preferences[20][4] = [5, 0, 15, 20] # player 3b
    preferences[20][5] = [20, 0, 5, 15] # player 4

# type (22):
    preferences[21][0] = [5, 0, 15, 20] # player 1
    preferences[21][1] = [15, 0, 20, 5] # player 2a
    preferences[21][2] = [5, 0, 20, 15] # player 2b
    preferences[21][3] = [15, 0, 20, 5] # player 3a
    preferences[21][4] = [5, 0, 20, 15] # player 3b
    preferences[21][5] = [20, 0, 15, 5] # player 4

# type (23):
    preferences[22][0] = [5, 15, 20, 0] # player 1
    preferences[22][1] = [15, 20, 5, 0] # player 2a
    preferences[22][2] = [5, 20, 15, 0] # player 2b
    preferences[22][3] = [15, 20, 5, 0] # player 3a
    preferences[22][4] = [5, 20, 15, 0] # player 3b
    preferences[22][5] = [20, 15, 5, 0] # player 4

# type (24):
    preferences[23][0] = [5, 15, 0, 20] # player 1
    preferences[23][1] = [15, 20, 0, 5] # player 2a
    preferences[23][2] = [5, 20, 0, 15] # player 2b
    preferences[23][3] = [15, 20, 0, 5] # player 3a
    preferences[23][4] = [5, 20, 0, 15] # player 3b
    preferences[23][5] = [20, 15, 0, 5] # player 4




    alternatives = ['blue', 'green', 'purple', 'orange']
    preferences[0][2] = [2, 20, 15, 5] # player 2b
    preferences[0][3] = [15, 20, 5, 2] # player 3a
    preferences[0][4] = [2, 20, 15, 5] # player 3b
    preferences[0][5] = [2, 5, 15, 20] # player 4

    # type (2):
    preferences[1][0] = [20, 15, 2, 5] # player 1
    preferences[1][1] = [15, 20, 2, 5] # player 2a
    preferences[1][2] = [2, 20, 5, 15] # player 2b
    preferences[1][3] = [15, 20, 2, 5] # player 3a
    preferences[1][4] = [2, 20, 5, 15] # player 3b
    preferences[1][5] = [2, 5, 20, 15] # player 4

    # type (3):
    preferences[2][0] = [20, 2, 15, 5] # player 1
    preferences[2][1] = [15, 2, 20, 5] # player 2a
    preferences[2][2] = [2, 5, 20, 15] # player 2b
    preferences[2][3] = [15, 2, 20, 5] # player 3a
    preferences[2][4] = [2, 5, 20, 15] # player 3b
    preferences[2][5] = [2, 20, 5, 15] # player 4

    # type (4):
    preferences[3][0] = [20, 2, 5, 15] # player 1
    preferences[3][1] = [15, 2, 5, 20] # player 2a
    preferences[3][2] = [2, 5, 15, 20] # player 2b
    preferences[3][3] = [15, 2, 5, 20] # player 3a
    preferences[3][4] = [2, 5, 15, 20] # player 3b
    preferences[3][5] = [2, 20, 15, 5] # player 4

    # type (5):
    preferences[4][0] = [20, 5, 15, 2] # player 1
    preferences[4][1] = [15, 5, 20, 2] # player 2a
    preferences[4][2] = [2, 15, 20, 5] # player 2b
    preferences[4][3] = [15, 5, 20, 2] # player 3a
    preferences[4][4] = [2, 15, 20, 5] # player 3b
    preferences[4][5] = [2, 15, 5, 20] # player 4

    # type (6):
    preferences[5][0] = [20, 5, 2, 15] # player 1
    preferences[5][1] = [15, 5, 2, 20] # player 2a
    preferences[5][2] = [2, 15, 5, 20] # player 2b
    preferences[5][3] = [15, 5, 2, 20] # player 3a
    preferences[5][4] = [2, 15, 5, 20] # player 3b
    preferences[5][5] = [2, 15, 20, 5] # player 4



    # type (7):
    preferences[6][0] = [15, 20, 5, 2] # player 1
    preferences[6][1] = [20, 15, 5, 2] # player 2a
    preferences[6][2] = [20, 2, 15, 5] # player 2b
    preferences[6][3] = [20, 15, 5, 2] # player 3a
    preferences[6][4] = [20, 2, 15, 5] # player 3b
    preferences[6][5] = [5, 2, 15, 20] # player 4


    # type (8):
    preferences[7][0] = [15, 20, 2, 5] # player 1
    preferences[7][1] = [20, 15, 2, 5] # player 2a
    preferences[7][2] = [20, 2, 5, 15] # player 2b
    preferences[7][3] = [20, 15, 2, 5] # player 3a
    preferences[7][4] = [20, 2, 5, 15] # player 3b
    preferences[7][5] = [5, 2, 20, 15] # player 4

    # type (9):
    preferences[8][0] = [15, 2, 20, 5] # player 1
    preferences[8][1] = [20, 2, 15, 5] # player 2a
    preferences[8][2] = [20, 5, 2, 15] # player 2b
    preferences[8][3] = [20, 2, 15, 5] # player 3a
    preferences[8][4] = [20, 5, 2, 15] # player 3b
    preferences[8][5] = [5, 20, 2, 15] # player 4

    # type (10):
    preferences[9][0] = [15, 2, 5, 20] # player 1
    preferences[9][1] = [20, 2, 5, 15] # player 2a
    preferences[9][2] = [20, 5, 15, 2] # player 2b
    preferences[9][3] = [20, 2, 5, 15] # player 3a
    preferences[9][4] = [20, 5, 15, 2] # player 3b
    preferences[9][5] = [5, 20, 15, 2] # player 4

    # type (11):
    preferences[10][0] = [15, 5, 20, 2] # player 1
    preferences[10][1] = [20, 5, 15, 2] # player 2a
    preferences[10][2] = [20, 15, 2, 5] # player 2b
    preferences[10][3] = [20, 5, 15, 2] # player 3a
    preferences[10][4] = [20, 15, 2, 5] # player 3b
    preferences[10][5] = [5, 15, 2, 20] # player 4

    # type (12):
    preferences[11][0] = [15, 5, 2, 20] # player 1
    preferences[11][1] = [20, 5, 2, 15] # player 2a
    preferences[11][2] = [20, 15, 5, 2] # player 2b
    preferences[11][3] = [20, 5, 2, 15] # player 3a
    preferences[11][4] = [20, 15, 5, 2] # player 3b
    preferences[11][5] = [5, 15, 20, 2] # player 4


    # type (13):
    preferences[12][0] = [5, 20, 15, 2] # player 1
    preferences[12][1] = [5, 15, 20, 2] # player 2a
    preferences[12][2] = [15, 2, 20, 5] # player 2b
    preferences[12][3] = [5, 15, 20, 2] # player 3a
    preferences[12][4] = [15, 2, 20, 5] # player 3b
    preferences[12][5] = [15, 2, 5, 20] # player 4


    # type (14):
    preferences[13][0] = [5, 20, 2, 15] # player 1
    preferences[13][1] = [5, 15, 2, 20] # player 2a
    preferences[13][2] = [15, 2, 5, 20] # player 2b
    preferences[13][3] = [5, 15, 2, 20] # player 3a
    preferences[13][4] = [15, 2, 5, 20] # player 3b
    preferences[13][5] = [15, 2, 20, 5] # player 4

    # type (15):
    preferences[14][0] = [5, 2, 20, 15] # player 1
    preferences[14][1] = [5, 2, 15, 20] # player 2a
    preferences[14][2] = [15, 5, 2, 20] # player 2b
    preferences[14][3] = [5, 2, 15, 20] # player 3a
    preferences[14][4] = [15, 5, 2, 20] # player 3b
    preferences[14][5] = [15, 20, 2, 5] # player 4

    # type (16):
    preferences[15][0] = [5, 15, 2, 20] # player 1
    preferences[15][1] = [5, 20, 2, 15] # player 2a
    preferences[15][2] = [15, 20, 5, 2] # player 2b
    preferences[15][3] = [5, 20, 2, 15] # player 3a
    preferences[15][4] = [15, 20, 5, 2] # player 3b
    preferences[15][5] = [15, 5, 20, 2] # player 4

    # type (17):
    preferences[16][0] = [5, 15, 20, 2] # player 1
    preferences[16][1] = [5, 20, 15, 2] # player 2a
    preferences[16][2] = [15, 20, 2, 5] # player 2b
    preferences[16][3] = [5, 20, 15, 2] # player 3a
    preferences[16][4] = [15, 20, 2, 5] # player 3b
    preferences[16][5] = [15, 5, 2, 20] # player 4

    # type (18):
    preferences[17][0] = [5, 15, 2, 20] # player 1
    preferences[17][1] = [5, 20, 2, 15] # player 2a
    preferences[17][2] = [15, 20, 5, 2] # player 2b
    preferences[17][3] = [5, 20, 2, 15] # player 3a
    preferences[17][4] = [15, 20, 5, 2] # player 3b
    preferences[17][5] = [15, 5, 20, 2] # player 4


    # type (19):
    preferences[18][0] = [2, 20, 15, 5] # player 1
    preferences[18][1] = [2, 15, 20, 5] # player 2a
    preferences[18][2] = [5, 2, 20, 15] # player 2b
    preferences[18][3] = [2, 15, 20, 5] # player 3a
    preferences[18][4] = [5, 2, 20, 15] # player 3b
    preferences[18][5] = [20, 2, 5, 15] # player 4

    # type (20):
    preferences[19][0] = [2, 20, 5, 15] # player 1
    preferences[19][1] = [2, 15, 5, 20] # player 2a
    preferences[19][2] = [5, 2, 15, 20] # player 2b
    preferences[19][3] = [2, 15, 5, 20] # player 3a
    preferences[19][4] = [5, 2, 15, 20] # player 3b
    preferences[19][5] = [20, 2, 15, 5] # player 4

    # type (21):
    preferences[20][0] = [2, 5, 20, 15] # player 1
    preferences[20][1] = [2, 5, 15, 20] # player 2a
    preferences[20][2] = [5, 15, 2, 20] # player 2b
    preferences[20][3] = [2, 5, 15, 20] # player 3a
    preferences[20][4] = [5, 15, 2, 20] # player 3b
    preferences[20][5] = [20, 15, 2, 5] # player 4

    # type (22):
    preferences[21][0] = [2, 5, 15, 20] # player 1
    preferences[21][1] = [2, 5, 20, 15] # player 2a
    preferences[21][2] = [5, 15, 20, 2] # player 2b
    preferences[21][3] = [2, 5, 20, 15] # player 3a
    preferences[21][4] = [5, 15, 20, 2] # player 3b
    preferences[21][5] = [20, 15, 5, 2] # player 4

    # type (23):
    preferences[22][0] = [2, 15, 20, 5] # player 1
    preferences[22][1] = [2, 20, 15, 5] # player 2a
    preferences[22][2] = [5, 20, 2, 15] # player 2b
    preferences[22][3] = [2, 20, 15, 5] # player 3a
    preferences[22][4] = [5, 20, 2, 15] # player 3b
    preferences[22][5] = [20, 5, 2, 15] # player 4

    # type (24):
    preferences[23][0] = [2, 15, 5, 20] # player 1
    preferences[23][1] = [2, 20, 5, 15] # player 2a
    preferences[23][2] = [5, 20, 15, 2] # player 2b
    preferences[23][3] = [2, 20, 5, 15] # player 3a
    preferences[23][4] = [5, 20, 15, 2] # player 3b
    preferences[23][5] = [20, 5, 15, 2] # player 4

    


    alternatives = ['blue', 'green', 'orange', 'purple']

    


class Subsession(BaseSubsession):
    # variable to determine the group level preference ordering
    Ordering = models.IntegerField(min=0,max=5)

    def set_order(self):
        self.Ordering = random.randint(0,Constants.num_profiles-1)

    def creating_session(self):
        self.group_randomly(fixed_id_in_group=False)

    # variables for paying round:
    paying_round = models.IntegerField(min=1,max=Constants.num_rounds,initial=0)
    def set_paying_round(self):
        p_round = random.randint(1,Constants.num_rounds)
        s = self.in_round(Constants.num_rounds)
        s.paying_round = p_round



class Group(BaseGroup):
    # variable to determine the group level preference ordering
    Ordering = models.IntegerField(min=0,max=5)

    def set_ordering(self):
        self.Ordering = self.subsession.Ordering

    Option1 = models.IntegerField(min=1,max=4,initial=0)
    Option2 = models.IntegerField(min=1,max=4,initial=0)
    Eliminated1 = models.IntegerField(min=1,max=4,initial=0)
    Eliminated2 = models.IntegerField(min=1,max=4,initial=0)

    def eliminate_alternatives(self):
        numeric_alternatives = [1, 2, 3, 4]
        random.shuffle(numeric_alternatives)
        remaining = [numeric_alternatives[0], numeric_alternatives[1]]
        remaining.sort()

        eliminated = [numeric_alternatives[2], numeric_alternatives[3]]
        eliminated.sort()


        self.Option1 = remaining[0]
        self.Option2 = remaining[1]
        self.Eliminated1 = eliminated[0]
        self.Eliminated2 = eliminated[1]


    Collective_Choice = models.IntegerField(min=0,max=3,initial=-1)
    def set_results(self):
        players = self.get_players()
        votes = [0 for x in range(0,4)]
        for p in players:
            votes[p.vote-1] = votes[p.vote-1]+1

        # checking whether the maximum is unique
        count = 0
        max_element = max(votes)
        for x in votes:
            if x >= max_element:
                count = count+1

        if count > 1:
            r = random.uniform(0,1)
            if r<=.5:
                self.Collective_Choice = self.Option1-1
            else:
                self.Collective_Choice = self.Option2-1
        else:
            self.Collective_Choice = votes.index(max(votes))
        players = self.get_players()
        for p in players:
            p.set_payoff()




class Player(BasePlayer):
    # variable to store the type:
    MyPreferences = models.IntegerField(min=0, max=5, initial=0)

    def set_MyPrefernces(self):
        # determining the deterministic types:
        if self.id_in_group == 1:
            self.MyPreferences = 0 
        if self.id_in_group == 4:
            self.MyPreferences = 5
        # determining the stochastic types:
        if self.id_in_group == 2:
            r = random.uniform(0,1)
            if r<=Constants.type_probability:
                self.MyPreferences = 1
            else:
                self.MyPreferences = 2
        if self.id_in_group == 3:
            r = random.uniform(0,1)
            if r<=Constants.type_probability:
                self.MyPreferences = 3
            else:
                self.MyPreferences = 4

    # variable to store the voting:
    vote  = models.IntegerField(min=0,max=4)
    earnings = models.IntegerField(min=0,max=20)

    # Setting payoffs for the voting treatment:
    def set_payoff(self):
        choice = self.group.Collective_Choice
        self.earnings = Constants.preferences[self.group.Ordering][self.MyPreferences][choice]
        if self.subsession.round_number == Constants.num_rounds:
            p = self.in_round(self.subsession.paying_round)
            self.payoff = p.earnings

    


    



 


