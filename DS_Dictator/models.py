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
Dominant Strategy Dictator Treatment
"""


class Constants(BaseConstants):
    name_in_url = 'DS_Dictator'
    players_per_group = 3
    num_rounds = 1

    # payoffs from the more and less preferred alternatives:
    high_payoff = 20
    low_payoff = 10

    # higher prob of the type profile
    prob_high = .9
    # moderate probability of the choice profile
    prob_mod = .5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 1
        if self.id_in_group == 2:
            return 2
        if self.id_in_group == 3:
            return 3






