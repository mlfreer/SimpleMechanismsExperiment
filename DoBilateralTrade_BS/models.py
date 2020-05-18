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
	num_rounds = 1
	# creating bounds for the support of the distribution of value:
	min_support = 0
	max_support = 100


class Subsession(BaseSubsession):

	def creating_session(self):
		# groupping people with the fixed roles (recall role is )
		#self.group_randomly(fixed_id_in_group=True)

		# setting the random prices:
		for g in self.get_groups():
			g.set_random_price()

		print('setting the value')
		# setting the values and the roles
		for p in self.get_players():
			#p.role()
			p.set_value()


class Group(BaseGroup):
	# in DS Bilateral Trade the price is determined as random:
	random_price = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	# method to support the random price:
	def set_random_price(self):
		# instead of using random.randrange that is for integers only, we use rand.uniform to have the float
		self.random_price = random.uniform(Constants.min_support,Constants.max_support)

	# setting payoffs function:
	def set_payoffs(self):
		p_buyer  = self.get_player_by_role('buyer')
		p_seller = self.get_player_by_role('seller')
		if p_buyer.personal_price >= self.random_price and p_seller.personal_price <= self.random_price:
			p_buyer.profit = p_buyer.value - self.random_price
			p_seller.profit = self.random_price - p_seller.value


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
		print('value set')




	# variables for the prices:
	personal_price = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	#buyer_price  = models.DecimalField(max_digits=5, decimal_places=1, default=0)

	# profit variable
	profit = models.DecimalField(max_digits=5, decimal_places=1, default=0)












