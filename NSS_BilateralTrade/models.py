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
The treatment contains the NonStrategically Simple Bilateral Trade Treatment
"""


class Constants(BaseConstants):
	name_in_url = 'NonStrategicallySimpleBilateralTrade'
	show_up_fee = 5 

	#constants for Risk aversion task:
	risk_return = 3
	risk_endowment = 2
	risk_exchange_rate = 1

	#constants for Beliefs:
	beliefs_revenue = 50

	# constants for Trade:
	trade_exchange_rate = .1

	players_per_group = 2
	num_rounds = 2  

	min_support = 0
	max_support = 100


class Subsession(BaseSubsession):
	# VARIABLES:
	# determining payoff of players
	paying_round = models.IntegerField()

	# FUNCTIONS:
	def creating_session(self):
		# groupping people with the fixed roles (recall role is )
		self.group_randomly(fixed_id_in_group=True)

		# setting the random prices:
		#for g in self.get_groups():
		#    g.set_random_price()

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
		self.final_price = (p_buyer.personal_price + p_seller.personal_price)/2
		if p_buyer.personal_price >= p_seller.personal_price:
			p_buyer.profit = p_buyer.value - self.final_price 
			p_seller.profit = self.final_price  - p_seller.value
		else:
			p_buyer.profit = 0
			p_seller.profit = 0
		# belief profit:
		p_buyer.set_belief_payoff()
		p_seller.set_belief_payoff()

	# setting final payoffs:
	def set_final_payoff(self):
		self.subsession.paying_round=random.randint(1,Constants.num_rounds)
		for p in self.get_players():
			# also converting to GBPs:
			p.final_treatment_profit = p.in_round(self.subsession.paying_round).profit*decimal.Decimal(Constants.trade_exchange_rate)
			p.final_beliefs_profit = p.in_round(self.subsession.paying_round).beliefs_profit*decimal.Decimal(Constants.trade_exchange_rate)



class Player(BasePlayer):
	# VARIABLES:
	# type of the player: 0 == seller; 1 == buyer
	def role(self):
		if self.id_in_group == 1:
			return 'buyer'
		if self.id_in_group == 2:
			return 'seller'
	# variables for the values
	value = models.DecimalField(max_digits=5, decimal_places=0, default=0)
	# variables for the prices:
	personal_price = models.DecimalField(max_digits=5, decimal_places=0, default=0)
	# profit variable
	profit = models.DecimalField(max_digits=5, decimal_places=0, default=0)

	# first order beliefs 
	fob = models.IntegerField()
	hit_fob = models.BooleanField(default=False)
	# second order beliefs 
	sob = models.IntegerField()
	hit_sob = models.BooleanField(default=False)
	# total profit form the beliefs treatment
	beliefs_profit = models.DecimalField(max_digits=5, decimal_places=0, default=0)

	# risk treatment variables
	risk_choice = models.DecimalField(max_digits=5, decimal_places=2, default=0, min=0, max=Constants.risk_endowment)
	risk_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	#payment info:
	#email input varaible:
	email = models.StringField()
	# show up fee
	show_up_fee = models.DecimalField(max_digits=5, decimal_places=2, default=Constants.show_up_fee)
	# profit from trade
	final_treatment_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	# profit form beliefs
	final_beliefs_profit = models.DecimalField(max_digits=5,decimal_places=2,default=0)
	# profit from the experiment 50/50 trade and beliefs
	final_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	# trade chosen for payment
	trade_chosen = models.BooleanField(default = False)


	# FUNCTIONS:
	# setting the values
	def set_value(self):    
		self.value = round(random.uniform(Constants.min_support,Constants.max_support),0)
		#print('value set')
	
	# functions defining the payoff
	def set_belief_payoff(self):
		self.beliefs_profit = 0
		self.hit_fob = False
		self.hit_sob = False
		for p in self.get_others_in_group():
			if (p.personal_price>= self.fob*10) and (p.personal_price<= (self.fob+2)*10):
				self.beliefs_profit = self.beliefs_profit+ Constants.beliefs_revenue
				self.hit_fob=True
			if (p.fob==self.sob):
				self.beliefs_profit = self.beliefs_profit+ Constants.beliefs_revenue
				self.hit_sob=True

	# setting payoffs for risk task:            
	def risk_results(self):
		r = random.uniform(0,1)
		risk_hold = Constants.risk_endowment-self.risk_choice
		if r>.5:
			self.risk_profit = Constants.risk_exchange_rate*(self.risk_choice*Constants.risk_return+risk_hold)
		else:
			self.risk_profit = risk_hold
	
	# setting final profit:
	def set_final_profit(self):
		# start with generating random number
		r = random.uniform(0,1)
		if r<=.5:
			self.final_profit = self.final_treatment_profit + self.risk_profit
			self.trade_chosen = True
		else:
			self.final_profit = self.risk_profit + self.final_beliefs_profit
			self.trade_chosen = False
		
		











