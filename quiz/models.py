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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None
    num_rounds = 1

    # quiz answers separated in blocks:
    a11 = 4
    a12 = 5
    a13 = 2
    a14 = 4
    a15 = 4

    a21 = 2
    a22 = 5
    a23 = 2
    a24 = 5
    a25 = 5

        # defining the vector of preferences:
    preferences = [[0 for x in range(0,6)] for x in range(0,6)]


    # type (4):
    preferences[0] = [15, 5, 0, 20] # player 1
    preferences[1] = [20, 15, 0, 5] # player 2a
    preferences[2] = [20, 5, 0, 15] # player 2b
    preferences[3] = [20, 15, 0, 5] # player 3a
    preferences[4] = [20, 5, 0, 15] # player 3b
    preferences[5] = [15, 20, 0, 5] # player 4

    alternatives = ['blue', 'green', 'purple', 'orange']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # variables for the quiz
    question = models.IntegerField()
