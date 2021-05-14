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
The treatment contains the Strategically Simple Bilateral Trade Treatment
"""


class Constants(BaseConstants):
	name_in_url = 'StrategicallySimpleBilateralTrade'
	show_up_fee = 5 

	#constants for Risk aversion task:
	risk_return = 3
	risk_endowment = 2
	risk_exchange_rate = 1


	#constants for Beliefs:
	beliefs_revenue = 3
	beliefs_probability_normalizer = 4

	# constants for Trade:
	trade_exchange_rate = .1

	min_support = 0
	max_support = 100

	players_per_group = 2
	num_rounds = 2  

class Subsession(BaseSubsession):

	def creating_session(self):
		# groupping people with the fixed roles (recall role is )
		self.group_randomly(fixed_id_in_group=True)

		# setting the random prices:
		#for g in self.get_groups():
		#	g.set_random_price()

		#print('setting the value')
		# setting the values and the roles
		for p in self.get_players():
			#p.role()
			p.set_value()


class Group(BaseGroup):
	# in DS Bilateral Trade the price is determined as random:
	final_price = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	

	# setting payoffs function:
	def set_payoffs(self):
		p_buyer  = self.get_player_by_role('buyer')
		p_seller = self.get_player_by_role('seller')
		self.final_price = p_seller.personal_price
		if p_buyer.personal_price >= p_seller.personal_price:
			p_buyer.profit = p_buyer.value - p_seller.personal_price
			p_seller.profit = p_seller.personal_price - p_seller.value
		else:
			p_buyer.profit = 0
			p_seller.profit = 0
		p_buyer.set_belief_payoff()
		p_seller.set_belief_payoff()



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

	final_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)


	#defining the belief related variables
	#fob = first order belief
	#sob = second order belief
	fob = models.IntegerField()
	# second order beliefs -- median
	sob = models.IntegerField()
	# total profit form the beliefs treatment
	beliefs_profit = models.DecimalField(max_digits=5, decimal_places=0, default=0)

	# functions defining the payoff
	def set_belief_payoff(self):
		self.beliefs_profit = 0
		for p in self.get_others_in_group():
			if (p.personal_price>= self.fob*10) and (p.personal_price<= (self.fob+2)*10):
				self.beliefs_profit = self.beliefs_profit+ Constants.beliefs_revenue
			if (p.fob==self.sob):
				self.beliefs_profit = self.beliefs_profit+ Constants.beliefs_revenue




	# part of the model which deals with the risk-aversion task
	risk_choice = models.DecimalField(max_digits=5, decimal_places=2, default=0, min=0, max=Constants.risk_endowment)

	risk_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	def risk_results(self):
		r = random.uniform(0,1)
		risk_hold = Constants.risk_endowment-self.risk_choice
		if r>.5:
			self.risk_profit = Constants.risk_exchange_rate*(self.risk_choice*Constants.risk_return+risk_hold)
		else:
			self.risk_profit = risk_hold


	#email input varaible:
	email = models.StringField()

	# show up fee
	show_up_fee = models.DecimalField(max_digits=5, decimal_places=2, default=Constants.show_up_fee)

	def set_final_profit(self):
		self.final_profit = self.final_treatment_profit + self.risk_profit + self.beliefs_profit










