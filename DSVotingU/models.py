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

    num_rounds = 2 # number of periods to be set to 10

    type_probability = .5 # probability of type of 2 and 3 being (a)

    # defining the vector of preferences:
    preferences = [[0 for x in range(0,6)] for x in range(0,6)]
    preferences[0] = [20, 15, 5, 0] # player 1
    preferences[1] = [5, 20, 15, 0] # player 2a
    preferences[2] = [15, 20, 5, 0] # player 2b
    preferences[3] = [5, 20, 15, 0] # player 3a
    preferences[4] = [15, 20, 5, 0] # player 3b
    preferences[5] = [5, 15, 20, 0] # player 4

    alternatives = ['blue', 'green', 'purple', 'red']
    # showup fee
    show_up_fee = 5

    # bc payoff:
    bc_payoff = 5

    # risk constants:
    risk_max = 20
    risk_min = 5
    risk_safe = 15
    risk_prob_winning = .5
    risk_prob_paying = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=False)

    # variables for paying round:
    paying_round = models.IntegerField(min=1,max=Constants.num_rounds,initial=0)
    def set_paying_round(self):
        p_round = random.randint(1,Constants.num_rounds)
        s = self.in_round(Constants.num_rounds)
        s.paying_round = p_round



class Group(BaseGroup):
    Option1 = models.IntegerField(min=1,max=4,initial=0)
    Option2 = models.IntegerField(min=1,max=4,initial=0)

    def eliminate_alternatives(self):
        numeric_alternatives = [1, 2, 3, 4]
        random.shuffle(numeric_alternatives)
        self.Option1 = numeric_alternatives[0]
        self.Option2 = numeric_alternatives[1]


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
        self.earnings = Constants.preferences[self.MyPreferences][choice]
        if self.subsession.round_number == Constants.num_rounds:
            p = self.in_round(self.subsession.paying_round)
            self.payoff = p.earnings

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

    def set_all_payoff(self):
        self.payoff = self.payoff + Constants.show_up_fee + self.risk_earnings + self.bc_earnings

    



 


