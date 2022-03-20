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
    name_in_url = 'FiveV_DS_U'
    players_per_group = 5

    num_rounds = 10 # number of periods to be set to 10

    type_probability = .5 # probability of type of 2 and 3 being (a)


    # number of profiles:
    num_profiles = 1

    # defining the vector of preferences:
    preferences = [[[0 for x in range(0,6)] for x in range(0,8)] for x in range(0,24)]

    # type (1):
    preferences[0][0] = [20, 15, 10, 1] # player 1
    preferences[0][1] = [15, 20, 10, 2] # player 2a
    preferences[0][2] = [10, 20, 15, 2] # player 2b
    preferences[0][3] = [15, 20, 10, 2] # player 3a
    preferences[0][4] = [10, 20, 15, 2] # player 3b
    preferences[0][5] = [15, 5, 4, 20] # player 4a
    preferences[0][6] = [4, 15, 5, 20] # player 4b
    preferences[0][7] = [1, 12, 20, 15] # player 5

    # list of alternatives:
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
        if self.id_in_group == 5:
            self.MyPreferences = 7
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
        if self.id_in_group == 4:
            r = random.uniform(0,1)
            if r<=Constants.type_probability:
                self.MyPreferences = 5
            else:
                self.MyPreferences = 6

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

    


    



 


