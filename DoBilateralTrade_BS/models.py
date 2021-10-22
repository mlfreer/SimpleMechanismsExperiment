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
	show_up_fee = 5	
	#constants for Risk aversion task:
	risk_return = 3
	risk_endowment = 2
	risk_exchange_rate = 1

	#constants for Beliefs:
	beliefs_revenue = 5

	# BC price:
	beauty_prize = 5

	# constants for Trade:
	trade_exchange_rate = 2

	players_per_group = 2
	num_rounds = 1

	min_support = 0
	max_support = 100	





class Subsession(BaseSubsession):
	# VARIABLES:
	# determining payoff of players
	paying_round = models.IntegerField()

	#-----------------------------------------------------------------------------
	# BEAUTY CONTEST PART:
	# FUNCTIONS:
	def set_prize(self):
		temp_sum = 0
		num_of_players = 0
		all_players = self.get_players()

		# computing the sum and number of players
		for p in all_players:
			temp_sum = temp_sum + p.my_guess
			num_of_players = num_of_players+1


		# computing the correct guess and personal distance.
		for p in all_players:
			p.goal_guess = ((2*temp_sum)/(3*num_of_players))
			p.my_distance = abs(p.my_guess - p.goal_guess)

		# determining min_distance:
		min_distance = 10000
		for p in all_players:
			if p.my_distance<min_distance:
				min_distance = p.my_distance

		# determining if p is winner:
		num_of_winners = 0
		for p in all_players:
			if p.my_distance == min_distance:
				p.is_winner=True
				num_of_winners = num_of_winners + 1

		for p in all_players:
			p.number_of_winners = num_of_winners
			if p.is_winner==True:
				p.my_prize = Constants.beauty_prize/num_of_winners

	#-----------------------------------------------------------------------------


	# FUNCTIONS:
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

	
	



class Group(BaseGroup):
	# VARIABLES:
	# in DS Bilateral Trade the price is determined as random:
	final_price = models.DecimalField(max_digits=5, decimal_places=0, default=0)
	paying_round = models.IntegerField()

	

	# FUNCTIONS:
	# method to support the random price:
	def set_random_price(self):
		# instead of using random.randrange that is for integers only, we use rand.uniform to have the float
		self.final_price = round(random.uniform(Constants.min_support,Constants.max_support),0)

	# setting payoffs function:
	def set_payoffs(self):
		# trade profit:
		p_buyer  = self.get_player_by_role('buyer')
		p_seller = self.get_player_by_role('seller')
		if p_buyer.personal_price >= self.final_price and p_seller.personal_price <= self.final_price:
			p_buyer.profit = p_buyer.value - self.final_price
			p_seller.profit = self.final_price - p_seller.value
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

	# risk part variables
	risk_choice = models.DecimalField(max_digits=5, decimal_places=2, default=0, min=0, max=Constants.risk_endowment)
	risk_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)



	#-----------------------------------------------------------------------------
	# BEAUTY CONTEST PART:

	# VARIABLES:
	my_guess = models.IntegerField(min=0, max=100)
	goal_guess = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	my_distance = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	is_winner = models.BooleanField(default=False)
	my_prize = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	number_of_winners = models.IntegerField()
	#-----------------------------------------------------------------------------



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
			if (p.personal_price>= self.fob*10) and (p.personal_price<= (self.fob+2)*10-1) or (p.personal_price==100 and self.fob == 8):
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
			self.final_profit = self.final_treatment_profit + self.risk_profit + decimal.Decimal(Constants.show_up_fee) + decimal.Decimal(self.my_prize)
			self.trade_chosen = True
		else:
			self.final_profit = self.risk_profit + self.final_beliefs_profit + decimal.Decimal(Constants.show_up_fee) + decimal.Decimal(self.my_prize)
			self.trade_chosen = False
		print(self.final_profit)
		self.payoff = self.final_profit
		
		












