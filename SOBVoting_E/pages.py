from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class SetupWaitPage(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        if self.subsession.round_number == 1:
            self.subsession.set_paying_round()
        players = self.subsession.get_players()
        self.subsession.set_order()
        for p in players: 
            p.set_MyPrefernces()
        groups = self.subsession.get_groups()
        for g in groups:
            g.set_ordering()
            g.set_menu()

class Voting(Page):
    form_model = 'player'
    form_fields = ['rank_1','rank_2','rank_3']

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
            my_profile = profile,
            my_preferences = temp,
            numeric_options = [self.group.Option1, self.group.Option2, self.group.Option3, self.group.Option4],
            options = [Constants.alternatives[self.group.Option1-1],Constants.alternatives[self.group.Option2-1],Constants.alternatives[self.group.Option3-1],Constants.alternatives[self.group.Option4-1]],
            round_number = self.player.subsession.round_number,
            num_rounds = Constants.num_rounds
            )
    def error_message(player, values):
        if (values['rank_1']<0) or (values['rank_2']<0) or (values['rank_3']<0):
            return "Please assign an alternative to each rank."
        if (values['rank_1']==values['rank_2']) or (values['rank_1']==values['rank_3']) or (values['rank_2']==values['rank_3']):
            return "Please assign a distinct alternative to each rank."


class VotingWaitPage(WaitPage):
    wait_for_all_groups = False
    def after_all_players_arrive(self):
        self.group.elimination_voting()


class Results(Page):
    def vars_for_template(self):
        if self.player.subsession.round_number == Constants.num_rounds:
            p = self.player.in_round(self.player.subsession.paying_round)
            self.player.participant.vars['treatment_earnings'] = p.earnings        

        profile = self.player.MyPreferences
        temp = [0 for x in range(0,4)]
        temp[0] = Constants.preferences[self.player.group.Ordering][profile][0]
        temp[1] = Constants.preferences[self.player.group.Ordering][profile][1]
        temp[2] = Constants.preferences[self.player.group.Ordering][profile][2]
        temp[3] = Constants.preferences[self.player.group.Ordering][profile][3]


        return dict(
            my_preferences = temp,
            preference_profiles = Constants.preferences[self.player.group.Ordering],
            my_number = self.player.id_in_group,
            my_profile = profile,
            collective_choice = Constants.alternatives[self.player.group.Collective_Choice],
            earnings = temp[self.player.group.Collective_Choice],
            numeric_collective_choice = self.player.group.Collective_Choice,
            round_number = self.player.subsession.round_number,
            num_rounds = Constants.num_rounds
            )


page_sequence = [SetupWaitPage, 
            Voting, 
            VotingWaitPage, 
            Results]
