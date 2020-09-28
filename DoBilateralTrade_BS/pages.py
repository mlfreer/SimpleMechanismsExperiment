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
	form_fields = ['personal_price']
	# always displayed
	def is_displayed(self):
		return True

	

class ResultsWaitPage(WaitPage):
	after_all_players_arrive = 'set_payoffs'
	#def after_all_players_arrive(self):
	#	self.player.group.set_payoffs()


class Results(Page):
	template_name ='DoBilateralTrade_BS/Results.html' 

class FOBInstructions(Page):
	template_name ='DoBilateralTrade_BS/FOBInstructions.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds 


class FOBInputPage(Page):
	template_name ='DoBilateralTrade_BS/FOBInputPage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	form_model = 'player'
	form_fields = ['fob_0','fob_20','fob_40','fob_60','fob_80']


class SOBInstructions(Page):
	template_name ='DoBilateralTrade_BS/SOBInstructions.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds 


class SOBInputPage(Page):
	template_name ='DoBilateralTrade_BS/SOBInputPage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	form_model = 'player'
	form_fields = ['sob_0','sob_20','sob_40','sob_60','sob_80']



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

class FinalPage(Page):
	template_name ='DoBilateralTrade_BS/FinalPage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	form_model = 'player'
	form_fields = ['email']

page_sequence = [WelcomePage, PriceInputPage, ResultsWaitPage, Results, FOBInstructions, FOBInputPage, SOBInstructions, SOBInputPage, RiskInstructions, RiskInputPage, FinalPage]




