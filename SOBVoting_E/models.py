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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'SOBVoting_E'
	players_per_group = None
	players_per_group = 4

	num_rounds = 10 # number of periods to be set to 10

	type_probability = .5 # probability of type of 2 and 3 being (a)

	# number of profiles:
	num_profiles = 1

	# defining the vector of preferences:
	preferences = [[[0 for x in range(0,6)] for x in range(0,6)] for x in range(0,24)]

	# type (1):
	preferences[0][0] = [20, 15, 5, 1] # player 1
	preferences[0][1] = [15, 20, 5, 1] # player 2a
	preferences[0][2] = [5, 20, 15, 1] # player 2b
	preferences[0][3] = [15, 20, 5, 1] # player 3a
	preferences[0][4] = [5, 20, 15, 1] # player 3b
	preferences[0][5] = [1, 5, 15, 20] # player 4

	
	alternatives = ['blue', 'green', 'orange', 'purple']



class Subsession(BaseSubsession):
	# variable to determine the group level preference ordering
	Ordering = models.IntegerField(min=0,max=5)

	def set_order(self):
		self.Ordering = random.randint(0,Constants.num_profiles-1)
		
	paying_round = models.IntegerField(min=1,max=Constants.num_rounds,initial=0)
	def set_paying_round(self):
		p_round = random.randint(1,Constants.num_rounds)
		s = self.in_round(Constants.num_rounds)
		s.paying_round = p_round


class Group(BaseGroup):
	Ordering = models.IntegerField(min=0,max=5)

	def set_ordering(self):
		self.Ordering = self.subsession.Ordering

	# defining the menu in the first stage:
	Option1 = models.IntegerField(min=1,max=4,initial=0)
	Option2 = models.IntegerField(min=1,max=4,initial=0)
	Option3 = models.IntegerField(min=1,max=4,initial=0)
	Option4 = models.IntegerField(min=1,max=4,initial=0)

	# collective choice variable:
	Collective_Choice = models.IntegerField(min=0,max=3,initial=-1)
	def set_menu(self):
		numeric_alternatives = [1, 2, 3, 4]

		self.Option1 = numeric_alternatives[0]
		self.Option2 = numeric_alternatives[1]
		self.Option3 = numeric_alternatives[2]
		self.Option4 = numeric_alternatives[3]


	def elimination_voting(self):
		players = self.get_players()
		menu_t0 = [self.Option1, self.Option2, self.Option4, self.Option4]

		# initially all alternatives are in the menu
		votes = [0 for i in range(0,4)]
		for p in players:
			votes[p.rank_1-1] = votes[p.rank_1-1]+1

		# eliminate the alternative collected maximum votes
		count = 0
		temp_index = [0 for x in range(0,4)]
		max_element = max(votes)
		k=0
		for x in votes:
			k=k+1
			if x >= max_element:
				temp_index[count] = k 
				count = count+1

		# controlling for possible ties:
		if count==1:
			stage0_Eliminated = temp_index[0]

		if count==2:
			r = random.uniform(0,1)
			if r<=.5:
				stage0_Eliminated = temp_index[0]
			else:
				stage0_Eliminated = temp_index[1]
			 
		if count==4:
			r = random.uniform(0,1)
			if r<=.25:
				stage0_Eliminated = temp_index[0]
			else:
				if r<=.5:
					stage0_Eliminated = temp_index[1]
				else:
					if r<=.75:
						stage0_Eliminated = temp_index[2]
					else:
						stage0_Eliminated = temp_index[3]

		# defining the remaining alternatives:
		numeric_alternatives = [1, 2, 3, 4]
		temp = [0 for x in range(0,3)]
		k=0
		for x in numeric_alternatives:
			if (x != stage0_Eliminated):
				temp[k] = x
				k=k+1
		stage1_Option1 = temp[0]
		stage1_Option2 = temp[1]
		stage1_Option3 = temp[2]
		print(temp)

		# run stage 2:
		menu_t1 = [stage1_Option1, stage1_Option2, stage1_Option3]
		for p in players:
			flag = 0
			for options in menu_t1:
				if p.rank_1 == options:
					flag = 1
					p.stage1_vote = p.rank_1
			if flag==0:
				for options in menu_t1:
					if p.rank_2 == options:
						flag = 1
						p.stage1_vote = p.rank_2
				if flag==0:
					for options in menu_t1:
						if p.rank_3 == options:
							flag = 1
							p.stage1_vote = p.rank_3

		# counting votes:
		votes = [0 for i in range(0,4)]
		for p in players:
			votes[p.stage1_vote-1] = votes[p.stage1_vote-1]+1

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
				stage1_Eliminated = temp_index[0]
			else:
				stage1_Eliminated = temp_index[1]
		else:
			stage1_Eliminated = temp_index[0]

		# defining the remaining alternatives:
		numeric_alternatives = [1, 2, 3, 4]
		temp = [0 for x in range(0,2)]
		k=0
		for x in numeric_alternatives:
			if (x != stage0_Eliminated) and (x != stage1_Eliminated):
				temp[k] = x
				k=k+1
		stage2_Option1 = temp[0]
		stage2_Option2 = temp[1]
		print(temp)


		# run stage 2:
		menu_t2 = [stage2_Option1, stage2_Option2]
		for p in players:
			flag = 0
			for options in menu_t2:
				if p.rank_1 == options:
					flag = 1
					p.stage2_vote = p.rank_1
			if flag==0:
				for options in menu_t2:
					if p.rank_2 == options:
						flag = 1
						p.stage2_vote = p.rank_2
				if flag==0:
					for options in menu_t2:
						if p.rank_3 == options:
							flag = 1
							p.stage2_vote = p.rank_3

		# counting votes:
		votes = [0 for i in range(0,4)]
		for p in players:
			votes[p.stage2_vote-1] = votes[p.stage2_vote-1]+1

		#checking whether the maximum is unique
		count = 0
		max_element = max(votes)
		for x in votes:
			if x >= max_element:
				count = count+1


		if count > 1:
			r = random.uniform(0,1)
			if r<=.5:
				stage2_Eliminated = stage2_Option1-1
			else:
				stage2_Eliminated = stage2_Option1-1
		else:
			stage2_Eliminated = votes.index(max(votes))

		if stage2_Eliminated == stage2_Option1-1:
			self.Collective_Choice = stage2_Option2-1
		else:
			self.Collective_Choice = stage2_Option1-1







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

	rank_1  = models.IntegerField(min=0,max=4)
	rank_2  = models.IntegerField(min=0,max=4)
	rank_3  = models.IntegerField(min=0,max=4)

	stage1_vote = models.IntegerField(min=0,max=4)
	stage2_vote = models.IntegerField(min=0,max=4)







