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
            g.random_elimination()


#class ResultsWaitPage(WaitPage):
#    pass

class VotingStage1(Page):
    form_model = 'player'
    form_fields = ['vote_stage1']
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
            eliminated = Constants.alternatives[self.group.stage1_Eliminated-1],
            numeric_options = [self.group.stage1_Option1, self.group.stage1_Option2, self.group.stage1_Option3],
            options = [Constants.alternatives[self.group.stage1_Option1-1],Constants.alternatives[self.group.stage1_Option2-1],Constants.alternatives[self.group.stage1_Option3-1]],
            round_number = self.player.subsession.round_number,
            num_rounds = Constants.num_rounds
            )


class VotingStage1WaitPage(WaitPage):
    wait_for_all_groups = False
    def after_all_players_arrive(self):
        self.group.eliminitation_voting_t1()

class VotingStage2(Page):
    form_model = 'player'
    form_fields = ['vote_stage2']
    def vars_for_template(self):
        profile = self.player.MyPreferences
        temp = [0 for x in range(0,4)]
        temp[0] = Constants.preferences[self.player.group.Ordering][profile][0]
        temp[1] = Constants.preferences[self.player.group.Ordering][profile][1]
        temp[2] = Constants.preferences[self.player.group.Ordering][profile][2]
        temp[3] = Constants.preferences[self.player.group.Ordering][profile][3]

        return dict(
            preference_profiles = Constants.preferences[self.player.group.Ordering],
            eliminated = Constants.alternatives[self.group.stage2_Eliminated-1],
            my_number = self.player.id_in_group,
            my_preferences = temp,
            my_profile = profile,
            numeric_options = [self.group.stage2_Option1, self.group.stage2_Option2],
            options = [Constants.alternatives[self.group.stage2_Option1-1],Constants.alternatives[self.group.stage2_Option2-1]],
            round_number = self.player.subsession.round_number,
            num_rounds = Constants.num_rounds
            )



class ResultsWaitPage(WaitPage):
    wait_for_all_groups = False
    def after_all_players_arrive(self):
        self.group.set_results()


class Results(Page):
    def vars_for_template(self):
        if self.player.subsession.round_number == Constants.num_rounds:
            p = self.player.in_round(self.player.subsession.paying_round)
            self.player.participant.vars['treatment_earnings'] = p.earnings        

        temp1 = [0 for x in range(0,4)]
        profile = self.player.MyPreferences
        temp1[0] = Constants.preferences[self.player.group.Ordering][profile][0]
        temp1[1] = Constants.preferences[self.player.group.Ordering][profile][1]
        temp1[2] = Constants.preferences[self.player.group.Ordering][profile][2]
        temp1[3] = Constants.preferences[self.player.group.Ordering][profile][3]


        return dict(
            my_preferences = temp1,
            my_profile = profile,
            preference_profiles = Constants.preferences[self.player.group.Ordering],
            my_number = self.player.id_in_group,
            collective_choice = Constants.alternatives[self.player.group.Collective_Choice],
            numeric_collective_choice = self.player.group.Collective_Choice,
            earnings = temp1[self.player.group.Collective_Choice],
            round_number = self.player.subsession.round_number,
            num_rounds = Constants.num_rounds
            )


page_sequence = [
                SetupWaitPage,
                VotingStage1,
                VotingStage1WaitPage,
                VotingStage2,
                ResultsWaitPage,
                Results,
                ]
