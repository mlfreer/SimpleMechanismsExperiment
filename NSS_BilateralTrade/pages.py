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
	form_fields = ['personal_price','fob','sob']


class ResultsWaitPage(WaitPage):
	after_all_players_arrive = 'set_payoffs'
	#def after_all_players_arrive(self):
	#	self.player.group.set_payoffs()


class Results(Page):
	template_name ='NSS_BilateralTrade/Results.html'
	def vars_for_template(self):
		return dict(
			lb_fob = self.player.fob*10,
			ub_fob = (self.player.fob+2)*10,
			lb_sob = self.player.sob*10,
			ub_sob = (self.player.sob+2)*10
			)



page_sequence = [WelcomePage, PriceInputPage, ResultsWaitPage, Results]
