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
    num_profiles = 12

    # defining the vector of preferences:
    preferences = [[[0 for x in range(0,6)] for x in range(0,6)] for x in range(0,12)]

    # randomized order of the preferences:
    # type (1):
    preferences[0][0] = [20, 15, 5, 0] # player 1
    preferences[0][1] = [5, 20, 15, 0] # player 2a
    preferences[0][2] = [15, 20, 5, 0] # player 2b
    preferences[0][3] = [5, 20, 15, 0] # player 3a
    preferences[0][4] = [15, 20, 5, 0] # player 3b
    preferences[0][5] = [5, 15, 20, 0] # player 4

    # type (2):
    preferences[1][0] = [0, 20, 15, 5] # player 1
    preferences[1][1] = [0, 5, 20, 15] # player 2a
    preferences[1][2] = [0, 15, 20, 5] # player 2b
    preferences[1][3] = [0, 5, 20, 15] # player 3a
    preferences[1][4] = [0, 15, 20, 5] # player 3b
    preferences[1][5] = [0, 5, 15, 20] # player 4

    # type (3):
    preferences[2][0] = [5, 0, 20, 15] # player 1
    preferences[2][1] = [15, 0, 5, 20] # player 2a
    preferences[2][2] = [5, 0, 15, 20] # player 2b
    preferences[2][3] = [15, 0, 5, 20] # player 3a
    preferences[2][4] = [5, 0, 15, 20] # player 3b
    preferences[2][5] = [20, 0, 5, 15] # player 4

    # type (4):
    preferences[3][0] = [15, 5, 0, 20] # player 1
    preferences[3][1] = [20, 15, 0, 5] # player 2a
    preferences[3][2] = [20, 5, 0, 15] # player 2b
    preferences[3][3] = [20, 15, 0, 5] # player 3a
    preferences[3][4] = [20, 5, 0, 15] # player 3b
    preferences[3][5] = [15, 20, 0, 5] # player 4

    # type (5):
    preferences[4][0] = [15, 20, 5, 0] # player 1
    preferences[4][1] = [20, 5, 15, 0] # player 2a
    preferences[4][2] = [20, 15, 5, 0] # player 2b
    preferences[4][3] = [20, 5, 15, 0] # player 3a
    preferences[4][4] = [20, 15, 5, 0] # player 3b
    preferences[4][5] = [15, 5, 20, 0] # player 4

    # type (6):
    preferences[5][0] = [15, 0, 20, 5] # player 1
    preferences[5][1] = [20, 0, 5, 15] # player 2a
    preferences[5][2] = [20, 0, 15, 5] # player 2b
    preferences[5][3] = [20, 0, 5, 15] # player 3a
    preferences[5][4] = [20, 0, 15, 5] # player 3b
    preferences[5][5] = [15, 0, 5, 20] # player 4

    # type (7):
    preferences[6][0] = [20, 5, 15, 0] # player 1
    preferences[6][1] = [5, 15, 20, 0] # player 2a
    preferences[6][2] = [15, 5, 20, 0] # player 2b
    preferences[6][3] = [5, 15, 20, 0] # player 3a
    preferences[6][4] = [15, 5, 20, 0] # player 3b
    preferences[6][5] = [5, 20, 15, 0] # player 4

    # type (8):
    preferences[7][0] = [20, 0, 5, 15] # player 1
    preferences[7][1] = [5, 0, 15, 20] # player 2a
    preferences[7][2] = [15, 0, 5, 20] # player 2b
    preferences[7][3] = [5, 0, 15, 20] # player 3a
    preferences[7][4] = [15, 0, 5, 20] # player 3b
    preferences[7][5] = [5, 0, 20, 15] # player 4

    # type (9):
    preferences[8][0] = [0, 15, 20, 5] # player 1
    preferences[8][1] = [0, 20, 5, 15] # player 2a
    preferences[8][2] = [0, 20, 15, 5] # player 2b
    preferences[8][3] = [0, 20, 5, 15] # player 3a
    preferences[8][4] = [0, 20, 15, 5] # player 3b
    preferences[8][5] = [0, 15, 5, 20] # player 4

    # type (10):
    preferences[9][0] = [0, 5, 15, 20] # player 1
    preferences[9][1] = [0, 15, 20, 5] # player 2a
    preferences[9][2] = [0, 5, 20, 15] # player 2b
    preferences[9][3] = [0, 15, 20, 5] # player 3a
    preferences[9][4] = [0, 5, 20, 15] # player 3b
    preferences[9][5] = [0, 20, 15, 5] # player 4

    # type (11):
    preferences[10][0] = [5, 20, 0, 15] # player 1
    preferences[10][1] = [15, 5, 0, 20] # player 2a
    preferences[10][2] = [5, 15, 0, 20] # player 2b
    preferences[10][3] = [15, 5, 0, 20] # player 3a
    preferences[10][4] = [5, 15, 0, 20] # player 3b
    preferences[10][5] = [20, 5, 0, 15] # player 4

    # type (12):
    preferences[11][0] = [5, 15, 20, 0] # player 1
    preferences[11][1] = [15, 20, 5, 0] # player 2a
    preferences[11][2] = [5, 20, 15, 0] # player 2b
    preferences[11][3] = [15, 20, 5, 0] # player 3a
    preferences[11][4] = [5, 20, 15, 0] # player 3b
    preferences[11][5] = [20, 15, 5, 0] # player 4



    alternatives = ['blue', 'green', 'purple', 'orange']

    


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

    


    



 


