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
Risk Elicitation Task
"""


class Constants(BaseConstants):
    name_in_url = 'RiskElicitation'
    players_per_group = None
    num_rounds = 1

    # risk constants:
    risk_max = 20
    risk_min = 5
    risk_safe = 15
    risk_prob_winning = .5
    risk_prob_paying = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Risk elicitation task
    risk_choice = models.IntegerField(min=0,max=1) # choice of the option in risk elicitation task 0 - safe, 1 - risky
    risk_earnings = models.IntegerField(min=0,max=20)


    def set_risk_results(self):
        #setting up the default:
        self.risk_earnings = 0
        # defining the payoffs:
        r1 = random.uniform(0,1)
        if r1<= Constants.risk_prob_paying:
            self.risk_earnings = Constants.risk_min
            if self.risk_choice == 0:
                self.risk_earnings = Constants.risk_safe
            else:
                r2 = random.uniform(0,1)
                if r2<=Constants.risk_prob_winning:
                    self.risk_earnings = Constants.risk_max    
        self.payoff = self.risk_earnings
