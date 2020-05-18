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
	prob_moderate = .5


class Subsession(BaseSubsession):

	def creating_session(self):
		# making sure that people are regroupped accordingly 
		self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
	CollectiveChoice = models.CharField(choices = ['A','B'])


class Player(BasePlayer):
	preference_profile = models.CharField(choices = ['AB','BA'])
 
	def role(self):
		if self.id_in_group == 1:
			return 1
		if self.id_in_group == 2:
			return 2
		if self.id_in_group == 3:
			return 3

	def set_preference_profile(self):
		if self.role == 1:
			r = random.uniform(0,1)
			if r > Constants.prob_high:
				preference_profile = 'BA'
			else:
				preference_profile = 'AB'
		if self.role == 2:
			r = random.uniform(0,1)
			if r > Constants.prob_moderate:
				preference_profile = 'BA'
			else:
				preference_profile = 'AB'
		if self.role == 3:
			r = random.uniform(0,1)
			if r > Constants.prob_high:
				preference_profile = 'AB'
			else:
				preference_profile = 'BA'

	# alternative to be chosen:
	chosen_alternative = models.CharField(choices = ['A','B'])
	# dictator to be chosen:
	chosen_dictator = models.IntegerField(widget = widgets.RadioSelect, 
		choices = self.group.get_others_in_group())







