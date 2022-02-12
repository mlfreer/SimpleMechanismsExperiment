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


#-----------------------------------------------------------------------------------
# quiz pages:
class Question1(Page):
	def is_displayed(self):
		return self.player.subsession.round_number == 1

	form_model  = 'player'
	form_fields = ['question']

	def vars_for_template(self):
		return dict(
			my_number = 1,
			my_profile = 0,
			my_preferences = Constants.preferences[3][0],
			preference_profiles = Constants.preferences[3]
			)

	form_show_errors = False

	def error_message(player, values):
		if values['question']!=Constants.a11:
			return 'error'


class Question2(Page):
	def is_displayed(self):
		return self.player.subsession.round_number == 1

	form_model  = 'player'
	form_fields = ['question']

	def vars_for_template(self):
		return dict(
			my_number = 1,
			my_profile = 0,
			my_preferences = Constants.preferences[3][0],
			preference_profiles = Constants.preferences[3]
			)

	form_show_errors = False

	def error_message(player, values):
		if values['question']!=Constants.a12:
			return 'error'
#-----------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------
# voting treatment page:
class SetupWaitPage(WaitPage):
	wait_for_all_groups = True
	def after_all_players_arrive(self):
		players = self.subsession.get_players()
		for p in players: 
			p.set_MyPrefernces()
		groups = self.subsession.get_groups()
		for g in groups:
			g.set_ordering()
			g.eliminate_alternatives()

class Voting(Page):
	form_model = 'player'
	form_fields = ['vote']
	def vars_for_template(self):
		profile = self.player.MyPreferences
		temp = [0 for x in range(0,4)]
		temp[0] = Constants.preferences[self.player.group.Ordering][profile][0]
		temp[1] = Constants.preferences[self.player.group.Ordering][profile][1]
		temp[2] = Constants.preferences[self.player.group.Ordering][profile][2]
		temp[3] = Constants.preferences[self.player.group.Ordering][profile][3]

		return dict(
			preference_profiles = Constants.preferences[self.player.group.Ordering],
			my_number = self.player.id_in_group,
			my_preferences = temp,
			my_profile = profile,
			numeric_options = [self.group.Option1, self.group.Option2],
			options = [Constants.alternatives[self.group.Option1-1],Constants.alternatives[self.group.Option2-1]],
			eliminated = [Constants.alternatives[self.group.Eliminated1-1],Constants.alternatives[self.group.Eliminated2-1]]
			)

class ResultsWaitPage(WaitPage):
	wait_for_all_groups = False
	def after_all_players_arrive(self):
		self.group.set_results()

class Results(Page):
	def vars_for_template(self):
		if self.player.subsession.round_number == Constants.num_rounds:
			self.player.participant.vars['treatment_earnings'] = self.player.earnings

		temp1 = [0 for x in range(0,4)]
		profile = self.player.MyPreferences
		temp1[0] = Constants.preferences[self.player.group.Ordering][profile][0]
		temp1[1] = Constants.preferences[self.player.group.Ordering][profile][1]
		temp1[2] = Constants.preferences[self.player.group.Ordering][profile][2]
		temp1[3] = Constants.preferences[self.player.group.Ordering][profile][3]


		return dict(
			my_preferences = temp1,
			preference_profiles = Constants.preferences[self.player.group.Ordering],
			my_number = self.player.id_in_group,
			my_profile = profile,
			collective_choice = Constants.alternatives[self.player.group.Collective_Choice],
			numeric_collective_choice = self.player.group.Collective_Choice,
			earnings = temp1[self.player.group.Collective_Choice]
			)

page_sequence = [Welcome, 
				# QUIZ:
				Question1,
				Question2,
				# voting treatment
				SetupWaitPage,
				Voting,
				ResultsWaitPage,
				Results,
				]
