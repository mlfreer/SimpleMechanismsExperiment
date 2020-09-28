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
The treatment contains the Dominant Strategy Bilateral Trade Treatment
"""


class Constants(BaseConstants):
	name_in_url = 'DominantStrategyBilateralTrade'
	players_per_group = 2
	num_rounds = 2
	# creating bounds for the support of the distribution of value:
	min_support = 0
	max_support = 100


class Subsession(BaseSubsession):

	def creating_session(self):
		# groupping people with the fixed roles (recall role is )
		self.group_randomly(fixed_id_in_group=True)

		# setting the random prices:
		for g in self.get_groups():
			g.set_random_price()

		#print('setting the value')
		# setting the values and the roles
		for p in self.get_players():
			#p.role()
			p.set_value()

	# determining payoff of players
	paying_round = models.IntegerField()
	



class Group(BaseGroup):
	# in DS Bilateral Trade the price is determined as random:
	final_price = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	paying_round = models.IntegerField()
	# method to support the random price:
	def set_random_price(self):
		# instead of using random.randrange that is for integers only, we use rand.uniform to have the float
		self.final_price = random.uniform(Constants.min_support,Constants.max_support)

	# setting payoffs function:
	def set_payoffs(self):
		p_buyer  = self.get_player_by_role('buyer')
		p_seller = self.get_player_by_role('seller')
		if p_buyer.personal_price >= self.final_price and p_seller.personal_price <= self.final_price:
			p_buyer.profit = p_buyer.value - self.final_price
			p_seller.profit = self.final_price - p_seller.value
		else:
			p_buyer.profit = 0
			p_seller.profit = 0

	def set_final_payoff(self):
		self.subsession.paying_round=random.randint(1,Constants.num_rounds)
		for p in self.get_players():
			p.final_treatment_profit = p.in_round(self.subsession.paying_round).profit



class Player(BasePlayer):
	# type of the player: 0 == seller; 1 == buyer
	def role(self):
		if self.id_in_group == 1:
			return 'buyer'
		if self.id_in_group == 2:
			return 'seller'

	# variables for the values
	value = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	#buyer_value  = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	# setting the values
	def set_value(self):
		self.value = random.uniform(Constants.min_support,Constants.max_support)
		#print('value set')

	# variables for the prices:
	personal_price = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	#buyer_price  = models.DecimalField(max_digits=5, decimal_places=1, default=0)

	# profit variable
	profit = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	final_treatment_profit = models.DecimalField(max_digits=5, decimal_places=1, default=0)



	#defining the belief related variables
	#fob = first order belief
	#sob = second order belief
	#belief comes with 5 vars corresponding to its own quantile

	# first order beliefs, defined witthe the lower bound of the interval.
	fob_0 = models.IntegerField(initial=0)
	fob_20 = models.IntegerField(initial=0)
	fob_40 = models.IntegerField(initial=0)
	fob_60 = models.IntegerField(initial=0)
	fob_80 = models.IntegerField(initial=0)

	fob_profit = models.DecimalField(max_digits=5, decimal_places=1, default=0)


	# second order beliefs, defined witthe the lower bound of the interval.
	sob_0 = models.IntegerField(initial=0)
	sob_20 = models.IntegerField(initial=0)
	sob_40 = models.IntegerField(initial=0)
	sob_60 = models.IntegerField(initial=0)
	sob_80 = models.IntegerField(initial=0)

	sob_profit = models.DecimalField(max_digits=5, decimal_places=1, default=0)



	# variable for the risk-aversion decision task
	risk_choice = models.DecimalField(max_digits=5, decimal_places=1, default=0)

	risk_profit = models.DecimalField(max_digits=5, decimal_places=1, default=0)

	#email input varaible:
	email = models.StringField()











