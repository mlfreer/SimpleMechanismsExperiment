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
    name_in_url = 'SOBVotingU'
    players_per_group = 4

    num_rounds = 5 # number of periods to be set to 10

    type_probability = .5 # probability of type of 2 and 3 being (a)

    # defining the vector of preferences:
    preferences = [[0 for x in range(0,6)] for x in range(0,6)]
    preferences[0] = [20, 15, 5, 0] # player 1
    preferences[1] = [5, 20, 15, 0] # player 2a
    preferences[2] = [15, 20, 5, 0] # player 2b
    preferences[3] = [5, 20, 15, 0] # player 3a
    preferences[4] = [15, 20, 5, 0] # player 3b
    preferences[5] = [5, 15, 20, 0] # player 4

    alternatives = ['W', 'X', 'Y', 'Z']


class Subsession(BaseSubsession):
    paying_round = models.IntegerField(min=1,max=Constants.num_rounds,initial=0)
    def set_paying_round(self):
        self.paying_round = random.randint(1,Constants.num_rounds)


class Group(BaseGroup):
    # defining the menu in the first stage:
    stage0_Option1 = models.IntegerField(min=1,max=4,initial=0)
    stage0_Option2 = models.IntegerField(min=1,max=4,initial=0)
    stage0_Option3 = models.IntegerField(min=1,max=4,initial=0)
    stage0_Option4 = models.IntegerField(min=1,max=4,initial=0)

    def set_menu(self):
        numeric_alternatives = [1, 2, 3, 4]
        random.shuffle(numeric_alternatives)
        self.stage0_Option1 = numeric_alternatives[0]
        self.stage0_Option2 = numeric_alternatives[1]
        self.stage0_Option3 = numeric_alternatives[2]
        self.stage0_Option4 = numeric_alternatives[3]


    # defining the alternatives present at the first stage voting:
    stage1_Option1 = models.IntegerField(min=1,max=4,initial=0)
    stage1_Option2 = models.IntegerField(min=1,max=4,initial=0)
    stage1_Option3 = models.IntegerField(min=1,max=4,initial=0)
    # alterantive eliminated at the first stage
    stage1_Eliminated = models.IntegerField(min=1,max=4,initial=0)
    def eliminitation_voting_t0(self):
        players = self.get_players()
        votes = [0 for x in range(0,4)]
        for p in players:
            votes[p.vote_stage0-1] = votes[p.vote_stage0-1]+1

        # checking whether the maximum is unique
        count = 0
        temp_index = [0 for x in range(0,4)]
        max_element = max(votes)
        k=0
        for x in votes:
            k=k+1

            if x >= max_element:
                temp_index[count] = k 
                count = count+1
        print(temp_index)

        # controlling for possible ties:
        if count==1:
            self.stage1_Eliminated = temp_index[0]

        if count==2:
            r = random.uniform(0,1)
            if r<=.5:
                self.stage1_Eliminated = temp_index[0]
            else:
                self.stage1_Eliminated = temp_index[1]
             
        if count==4:
            r = random.uniform(0,1)
            if r<=.25:
                self.stage1_Eliminated = temp_index[0]
            else:
                if r<=.5:
                    self.stage1_Eliminated = temp_index[1]
                else:
                    if r<=.75:
                        self.stage1_Eliminated = temp_index[2]
                    else:
                        self.stage1_Eliminated = temp_index[3]

        

        # defining the remaining alternatives:
        numeric_alternatives = [1, 2, 3, 4]
        temp = [0 for x in range(0,3)]
        k=0
        for x in numeric_alternatives:
            if (x != self.stage1_Eliminated):
                temp[k] = x
                k=k+1
        self.stage1_Option1 = temp[0]
        self.stage1_Option2 = temp[1]
        self.stage1_Option3 = temp[2]
        print(temp)




    #defining the alternatives present at the second stage voting:
    stage2_Eliminated = models.IntegerField(min=1,max=4,initial=0)
    stage2_Option1 = models.IntegerField(min=1,max=4,initial=0)
    stage2_Option2 = models.IntegerField(min=1,max=4,initial=0)
    def eliminitation_voting_t1(self):
        # counting the votes
        players = self.get_players()
        votes = [0 for x in range(0,4)]
        for p in players:
            votes[p.vote_stage1-1] = votes[p.vote_stage1-1]+1

        # accounting for previously eliminated alternative:
        votes[self.stage1_Eliminated-1] = -10

        # checking whether the maximum is unique
        count = 0
        temp_index = [0 for x in range(0,2)]
        max_element = max(votes)
        k=0
        for x in votes:
            k=k+1
            if x >= max_element:
                temp_index[count] = k 
                count = count+1
        print(temp_index)

        if count>1:
            r = random.uniform(0,1)
            if r<=.5:
                self.stage2_Eliminated = temp_index[0]
            else:
                self.stage2_Eliminated = temp_index[1]
        else:
            self.stage2_Eliminated = temp_index[0]

        # defining the remaining alternatives:
        numeric_alternatives = [1, 2, 3, 4]
        temp = [0 for x in range(0,2)]
        k=0
        for x in numeric_alternatives:
            if (x != self.stage1_Eliminated) and (x != self.stage2_Eliminated):
                temp[k] = x
                k=k+1
        self.stage2_Option1 = temp[0]
        self.stage2_Option2 = temp[1]
        print(temp)


    # computing the voting results at t=2
    Collective_Choice = models.IntegerField(min=0,max=3,initial=-1)
    def set_results(self):
        players = self.get_players()
        votes = [0 for x in range(0,4)]
        for p in players:
            votes[p.vote_stage2-1] = votes[p.vote_stage2-1]+1

        # checking whether the maximum is unique
        count = 0
        max_element = max(votes)
        for x in votes:
            if x >= max_element:
                count = count+1

        if count > 1:
            r = random.uniform(0,1)
            if r<=.5:
                self.Collective_Choice = self.stage2_Option1-1
            else:
                self.Collective_Choice = self.stage2_Option1-1
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
    vote_stage0  = models.IntegerField(min=0,max=4)
    vote_stage1  = models.IntegerField(min=0,max=4)
    vote_stage2  = models.IntegerField(min=0,max=4)
    earnings = models.IntegerField(min=0,max=20)

    def set_payoff(self):
        choice = self.group.Collective_Choice
        self.earnings = Constants.preferences[self.MyPreferences][choice]
        if self.subsession.round_number == self.subsession.paying_round:
            p = self.in_round(Constants.num_rounds)
            p.payoff = self.earnings


 


