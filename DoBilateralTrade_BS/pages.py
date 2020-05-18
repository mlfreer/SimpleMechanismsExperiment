from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
	template_name ='DoBilateralTrade_BS/WelcomePage.html'
	def is_displayed(self):
		return self.player.subsession.round_number == 1

class PriceInputPage(Page):
	template_name ='DoBilateralTrade_BS/PriceInputPage'
	# always displayed
	def is_displayed(self):
		return True

	form_models = models.Player
	form_fields = ['personal_price']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
    	self.player.group.set_payoffs()


class Results(Page):
    template_name ='DoBilateralTrade_BS/Results'


page_sequence = [WelcomePage, PriceInputPage, ResultsWaitPage, Results]
