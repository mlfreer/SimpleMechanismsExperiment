from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
	template_name ='NSS_BilateralTrade/WelcomePage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == 1

	#after_all_players_arrive = 'player.set_value'

class PriceInputPage(Page):
	template_name ='NSS_BilateralTrade/PriceInputPage.html'
	# always displayed
	def is_displayed(self):
		return True

	form_model = 'player'
	form_fields = ['personal_price']


class ResultsWaitPage(WaitPage):
	after_all_players_arrive = 'set_payoffs'
    #def after_all_players_arrive(self):
    #	self.player.group.set_payoffs()


class Results(Page):
    template_name ='NSS_BilateralTrade/Results.html'



class BeliefsInputPage(Page):
	template_name ='NSS_BilateralTrade/BeliefsInputPage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	form_model = 'player'
	form_fields = ['fob_0','fob_20','fob_40','fob_60','fob_80','sob_0','sob_20','sob_40','sob_60','sob_80']


page_sequence = [WelcomePage, PriceInputPage, ResultsWaitPage, Results, BeliefsInputPage]
