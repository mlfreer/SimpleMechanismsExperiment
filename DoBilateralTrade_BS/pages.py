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
    template_name ='DoBilateralTrade_BS/Results.html' 

page_sequence = [WelcomePage, PriceInputPage, ResultsWaitPage, Results]
