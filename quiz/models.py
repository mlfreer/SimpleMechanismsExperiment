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

    # Treatments
    DominantStrategy = 1
    FirstOrder = 2
    SecondOrder = 3

    # quiz answers separated in blocks:

    # block 1: preferences, exampe 1
    a11 = 4
    a12 = 5
    a13 = 2
    a14 = 4
    a15 = 4

    # block 2: preferences example 2
    a21 = 2
    a22 = 5
    a23 = 2
    a24 = 5
    a25 = 5

    # block 3: Stage 1 voting (SOB)
    a31 = 2
    a32 = 5
    a33 = 1
    a34 = 5

    # block 4: Stage 2 voting (SOB) or Stage 1 voting (FOB)
    a41 = 2
    a42 = 5
    a43 = 1

    # block 5: Stage 3 voting (SOB) or Stage 2 voting (FOB) or Stage 1 voting (DS)
    a51 = 2
    a52 = 5

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
    question_number = models.IntegerField(initial=1)
