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
	bliefs_revenue = 2.5

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
	final_price = models.DecimalField(max_digits=5, decimal_places=0, default=0)
	paying_round = models.IntegerField()
	# method to support the random price:
	def set_random_price(self):
		# instead of using random.randrange that is for integers only, we use rand.uniform to have the float
		self.final_price = round(random.uniform(Constants.min_support,Constants.max_support),0)

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
			# also converting to GBPs:
			p.final_treatment_profit = p.in_round(self.subsession.paying_round).profit*decimal.Decimal(Constants.trade_exchange_rate)



class Player(BasePlayer):
	# type of the player: 0 == seller; 1 == buyer
	def role(self):
		if self.id_in_group == 1:
			return 'buyer'
		if self.id_in_group == 2:
			return 'seller'

	# variables for the values
	value = models.DecimalField(max_digits=5, decimal_places=0, default=0)
	#buyer_value  = models.DecimalField(max_digits=5, decimal_places=1, default=0)
	# setting the values
	def set_value(self):	
		self.value = round(random.uniform(Constants.min_support,Constants.max_support),0)
		#print('value set')

	# variables for the prices:
	personal_price = models.DecimalField(max_digits=5, decimal_places=0, default=0)
	#buyer_price  = models.DecimalField(max_digits=5, decimal_places=1, default=0)

	# profit variable
	profit = models.DecimalField(max_digits=5, decimal_places=0, default=0)

	final_treatment_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	final_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)


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

	fob_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)


	# second order beliefs, defined witthe the lower bound of the interval.
	sob_0 = models.IntegerField(initial=0)
	sob_20 = models.IntegerField(initial=0)
	sob_40 = models.IntegerField(initial=0)
	sob_60 = models.IntegerField(initial=0)
	sob_80 = models.IntegerField(initial=0)

	sob_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	# total profit form the beliefs treatment
	beliefs_profit = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	# functions defining the payoff
	def set_belief_payoff(self):
		# defining the random number for both treatments
		fob_r = random.uniform(0,1)
		sob_r = random.uniform(0,1)

		# randomly selecting the interval (1..5)
		fob_rint = random.randint(1,5)
		sob_rint = random.randint(1,5)

		# determining number of groups:
		num_of_groups = self.session.num_participants/Constants.players_per_group

		# fob_int = number of the quintile to be used
		# fob_sol = belief in this quintile
		if fob_rint == 1:
			fob_int = 1
			fob_sol = self.fob_0
		elif fob_rint == 2:
			fob_int = 2
			fob_sol = self.fob_20
		elif fob_rint == 3:
			fob_int = 1
			fob_sol = self.fob_40
		elif fob_rint == 4:
			fob_int = 4
			fob_sol = self.fob_60
		else:
			fob_int = 5
			fob_sol = self.fob_80


		# fob_int = number of the quintile to be used
		# fob_sol = belief in this quintile
		if sob_rint == 1:
			sob_int = 1
			sob_sol = self.sob_0
		elif sob_rint == 2:
			sob_int = 2
			sob_sol = self.sob_20
		elif sob_rint == 3:
			sob_int = 1
			sob_sol = self.sob_40
		elif sob_rint == 4:
			sob_int = 4
			sob_sol = self.sob_60
		else:
			sob_int = 5
			sob_sol = self.sob_80

		if fob_r > fob_sol:
			random_number = random.uniform(0,1)
			if random_number<=fob_r:
				self.fob_profit = Constants.bliefs_revenue
			else:
				self.fob_profit = 0
		else:
			rand_period = random.randint(1,Constants.num_rounds)
			rand_group = random_randint(1,num_of_groups)

			# choosing random period
			chosen_s = self.subsession.in_round(rand_period)

			# choosing random group
			for g in chosen_s.get_groups():
				if g.id_in_subsession == rand_group:
					chosen_g = g
			

			# choosing random player
			if self.role == 'buyer':
				chosen_p = g.get_player_by_role('seller')
			else:
				chosen_p = g.get_player_by_role('buyer')

			if chosen_p.personal_price >= (i-1)*20 and chosen_p.personal_price <= i*20:
				self.fob_profit = Constants.bliefs_revenue
			else:
				self.fob_profit = 0

		#temp fix:
		self.sob_profit = 0
		self.beliefs_profit = self.fob_profit + self.sob_profit










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












