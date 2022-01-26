from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# welcome page:
class Welcome(Page):
	template_name ='DSVotingU/Welcome.html'
	def is_displayed(self):
		return self.player.subsession.round_number == 1
	def before_next_page(self):
		self.player.subsession.set_paying_round()


# voting treatment page:
class SetupWaitPage(WaitPage):
	wait_for_all_groups = True
	def after_all_players_arrive(self):
		players = self.subsession.get_players()
		for p in players: 
			p.set_MyPrefernces()
		groups = self.subsession.get_groups()
		for g in groups:
			g.eliminate_alternatives()

class Voting(Page):
	form_model = 'player'
	form_fields = ['vote']
	def vars_for_template(self):
		profile = self.player.MyPreferences
		temp = [0 for x in range(0,4)]
		temp[0] = Constants.preferences[profile][0]
		temp[1] = Constants.preferences[profile][1]
		temp[2] = Constants.preferences[profile][2]
		temp[3] = Constants.preferences[profile][3]

		return dict(
			preference_profiles = Constants.preferences,
			my_number = self.player.id_in_group,
			my_preferences = temp,
			my_profile = profile,
			numeric_options = [self.group.Option1, self.group.Option2],
			options = [Constants.alternatives[self.group.Option1-1],Constants.alternatives[self.group.Option2-1]]
			)

class ResultsWaitPage(WaitPage):
	wait_for_all_groups = False
	def after_all_players_arrive(self):
		self.group.set_results()

class Results(Page):
	def vars_for_template(self):
		temp1 = [0 for x in range(0,4)]
		profile = self.player.MyPreferences
		temp1[0] = Constants.preferences[profile][0]
		temp1[1] = Constants.preferences[profile][1]
		temp1[2] = Constants.preferences[profile][2]
		temp1[3] = Constants.preferences[profile][3]


		return dict(
			my_preferences = temp1,
			preference_profiles = Constants.preferences,
			my_number = self.player.id_in_group,
			my_profile = profile,
			collective_choice = Constants.alternatives[self.player.group.Collective_Choice],
			numeric_collective_choice = self.player.group.Collective_Choice,
			earnings = temp1[self.player.group.Collective_Choice]
			)




# page with final results:
class FinalResults(Page):
	def is_displayed(self):
		return self.player.subsession.round_number == Constants.num_rounds

	def vars_for_template(self):
		p = self.player.in_round(self.subsession.paying_round)
		return dict(
			earning = c(p.earnings),
			show_up_fee = c(5),
			beauty_contest  = c(self.player.bc_earnings),
			risk = c(self.player.risk_earnings),
			payoff = self.player.payoff
			)


page_sequence = [Welcome, 
				# voting treatment
				SetupWaitPage,
				Voting,
				ResultsWaitPage,
				Results,
				# final results
				FinalResults
				]
