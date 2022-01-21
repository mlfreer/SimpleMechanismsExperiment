from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
	template_name ='DSVotingU/Welcome.html'
	def is_displayed(self):
		return self.player.subsession.round_number == 1

class SetupWaitPage(WaitPage):
	wait_for_all_groups = True
	def after_all_players_arrive(self):
		players = self.player.subsession.get_players()
		for p in players: 
			p.set_MyPrefernces()


#class ResultsWaitPage(WaitPage):
#    pass

class Voting(Page):
	pass


class Results(Page):
	def vars_for_template(self):
		temp1 = [0 for x in range(0,4)]
		profile = self.player.MyPreferences
		temp1[0] = Constants.preferences[profile][0]
		temp1[1] = Constants.preferences[profile][1]
		temp1[2] = Constants.preferences[profile][2]
		temp1[3] = Constants.preferences[profile][3]

		return dict(
			profile = self.player.MyPreferences,
			pref_profile = temp1,
			array = range(0,4)
			)



page_sequence = [Welcome, 
				SetupWaitPage,
				#Voting,
				Results]
