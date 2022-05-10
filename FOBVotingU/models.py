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
	name_in_url = 'FOBVotingU'
	players_per_group = 4

	num_rounds = 10 # number of periods to be set to 10

	type_probability = .5 # probability of type of 2 and 3 being (a)

	# number of profiles:
	num_profiles = 1

	# defining the vector of preferences:
	preferences = [[[0 for x in range(0,6)] for x in range(0,6)] for x in range(0,24)]

	# randomized order of the preferences:
	# type (1):
	preferences[0][0] = [20, 15, 5, 1] # player 1
	preferences[0][1] = [15, 20, 5, 1] # player 2a
	preferences[0][2] = [5, 20, 15, 1] # player 2b
	preferences[0][3] = [15, 20, 5, 1] # player 3a
	preferences[0][4] = [5, 20, 15, 1] # player 3b
	preferences[0][5] = [1, 5, 15, 20] # player 4


	
	alternatives = ['blue', 'green', 'orange', 'purple']


class Subsession(BaseSubsession):

	Ordering = models.IntegerField(min=0,max=5)

	def set_order(self):
		self.Ordering = random.randint(0,Constants.num_profiles-1)

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

	# defining the alternatives present at the first stage voting:
	stage1_Option1 = models.IntegerField(min=1,max=4,initial=0)
	stage1_Option2 = models.IntegerField(min=1,max=4,initial=0)
	stage1_Option3 = models.IntegerField(min=1,max=4,initial=0)

	# alterantive eliminated at the first stage
	stage1_Eliminated = models.IntegerField(min=1,max=4,initial=0)
	def random_elimination(self):
		numeric_alternatives = [1, 2, 3, 4]
		random.shuffle(numeric_alternatives)

		remaining = [numeric_alternatives[0], numeric_alternatives[1], numeric_alternatives[2]]
		remaining.sort()

		eliminated = [numeric_alternatives[3]]
		eliminated.sort()

		self.stage1_Option1 = remaining[0]
		self.stage1_Option2 = remaining[1]
		self.stage1_Option3 = remaining[2]
		self.stage1_Eliminated = eliminated[0]

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
			if x >= max_element:
				temp_index[count] = k 
				count = count+1
			k=k+1

		if count>1:
			r = random.uniform(0,1)
			if r<=.5:
				self.stage2_Eliminated = temp_index[0]+1
			else:
				self.stage2_Eliminated = temp_index[1]+1
		else:
			self.stage2_Eliminated = votes.index(max(votes))+1

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


	# computing the voting results at t=2
	stage3_Eliminated = models.IntegerField(min=1,max=4,initial=0)
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
				self.stage3_Eliminated = self.stage2_Option1-1
			else:
				self.stage3_Eliminated = self.stage2_Option1-1
		else:
			self.stage3_Eliminated = votes.index(max(votes))

		if self.stage3_Eliminated == self.stage2_Option1-1:
			self.Collective_Choice = self.stage2_Option2-1
		else:
			self.Collective_Choice = self.stage2_Option1-1

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
	vote_stage1  = models.IntegerField(min=0,max=4)
	vote_stage2  = models.IntegerField(min=0,max=4)
	earnings = models.IntegerField(min=0,max=20)

	def set_payoff(self):
		choice = self.group.Collective_Choice
		self.earnings = Constants.preferences[self.group.Ordering][self.MyPreferences][choice]
		if self.subsession.round_number == Constants.num_rounds:
			p = self.in_round(Constants.num_rounds)
			self.payoff = p.earnings


 


