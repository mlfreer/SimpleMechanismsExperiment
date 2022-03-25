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

    # block 1: preferences, exampe 1
    a11 = 3
    a12 = 2
    a13 = 3
    a14 = 3
    a15 = 3
    a21 = 7

        # defining the vector of preferences:
    preferences = [[0 for x in range(0,6)] for x in range(0,6)]


# type (5):
    preferences[0] = [20, 5, 15, 2] # player 1
    preferences[1] = [15, 5, 20, 2] # player 2a
    preferences[2] = [2, 15, 20, 5] # player 2b
    preferences[3] = [15, 5, 20, 2] # player 3a
    preferences[4] = [2, 15, 20, 5] # player 3b
    preferences[5] = [2, 15, 5, 20] # player 4

    alternatives = ['blue', 'green', 'orange', 'purple',]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # variables for the quiz
    question = models.IntegerField()
    question_number = models.IntegerField(initial=1)
