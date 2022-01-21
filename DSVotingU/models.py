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


author = 'Mikhail Freer'

doc = """
The code for the Dominant Strategy Voting Treatment with Unequal Strategy Space (DSxU treatment)
"""


class Constants(BaseConstants):
    name_in_url = 'DSVotingU'
    players_per_group = 4

    num_rounds = 1 # number of periods to be set to 10

    type_probability = .5 # probability of type of 2 and 3 being (a)

    # defining the vector of preferences:
    preferences = [[0 for x in range(0,6)] for x in range(0,6)]
    preferences[0] = [20, 15, 5, 0] # player 1
    preferences[1] = [15, 20, 5, 0] # player 2a
    preferences[2] = [15, 20, 5, 0] # player 2b
    preferences[3] = [15, 20, 5, 0] # player 3a
    preferences[4] = [15, 20, 5, 0] # player 3b
    preferences[5] = [5, 15, 20, 0] # player 4



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # variable to store the type:
    MyPreferences = models.IntegerField(min=0, max=5, initial=0)

    def set_MyPrefernces(self):
        # determining the deterministic types:
        if self.id_in_group == 1:
            MyPreferences = 0 
        if self.id_in_group == 4:
            MyPreferences = 5
        # determining the stochastic types:
        if self.id_in_group == 2:
            r = random.uniform(0,1)
            if r<=Constants.type_probability:
                MyPreferences = 1
            else:
                MyPreferences = 2
        if self.id_in_group == 3:
            r = random.uniform(0,1)
            if r<=Constants.type_probability:
                MyPreferences = 3
            else:
                MyPreferences = 4

    # variable to store the voting:
    Vote  = models.IntegerField(min=0,max=5)

 


