from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
	template_name ='DoBilateralTrade_BS/WelcomePage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == 1

	#after_all_players_arrive = 'player.set_value'

class PriceInputPage(Page):
	template_name ='DoBilateralTrade_BS/PriceInputPage.html'

	form_model = 'player'
	form_fields = ['personal_price','fob','sob']
	# always displayed
	def is_displayed(self):
		return True

	

class ResultsWaitPage(WaitPage):
	after_all_players_arrive = 'set_payoffs'
	#def after_all_players_arrive(self):
	#	self.player.group.set_payoffs()


class Results(Page):
	template_name ='DoBilateralTrade_BS/Results.html' 
	def vars_for_template(self):
		return dict(
			lb_fob = self.player.fob*10,
			ub_fob = (self.player.fob+2)*10,
			lb_sob = self.player.sob*10,
			ub_sob = (self.player.sob+2)*10
			)


class EarningsWaitPage(WaitPage):
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds 

	after_all_players_arrive = 'set_final_payoff'




class RiskInstructions(Page):
	template_name ='DoBilateralTrade_BS/RiskInstructions.html' 
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds




class RiskInputPage(Page):
	template_name ='DoBilateralTrade_BS/RiskInputPage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	form_model = 'player'
	form_fields = ['risk_choice']

	def before_next_page(self):
		self.player.risk_results()
		self.player.set_final_profit()

class FinalPage(Page):
	template_name ='DoBilateralTrade_BS/FinalPage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	form_model = 'player'
	form_fields = ['email']

page_sequence = [WelcomePage, PriceInputPage, ResultsWaitPage, Results, EarningsWaitPage, RiskInstructions, RiskInputPage, FinalPage]




