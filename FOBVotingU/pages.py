from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    template_name ='DSVotingU/Welcome.html'
    def is_displayed(self):
        return self.player.subsession.round_number == 1
    def before_next_page(self):
        self.player.subsession.set_paying_round()

class SetupWaitPage(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        players = self.subsession.get_players()
        for p in players: 
            p.set_MyPrefernces()
        groups = self.subsession.get_groups()
        for g in groups:
            g.random_elimination()


#class ResultsWaitPage(WaitPage):
#    pass

class VotingStage1(Page):
    form_model = 'player'
    form_fields = ['vote_stage1']
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
            numeric_options = [self.group.stage1_Option1, self.group.stage1_Option2, self.group.stage1_Option3],
            options = [Constants.alternatives[self.group.stage1_Option1-1],Constants.alternatives[self.group.stage1_Option2-1],Constants.alternatives[self.group.stage1_Option3-1]]
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
        temp[0] = Constants.preferences[profile][0]
        temp[1] = Constants.preferences[profile][1]
        temp[2] = Constants.preferences[profile][2]
        temp[3] = Constants.preferences[profile][3]

        return dict(
            preference_profiles = Constants.preferences,
            eliminated = Constants.alternatives[self.group.stage2_Eliminated-1],
            my_number = self.player.id_in_group,
            my_preferences = temp,
            numeric_options = [self.group.stage2_Option1, self.group.stage2_Option2],
            options = [Constants.alternatives[self.group.stage2_Option1-1],Constants.alternatives[self.group.stage2_Option2-1]]
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
            collective_choice = Constants.alternatives[self.player.group.Collective_Choice],
            earnings = temp1[self.player.group.Collective_Choice]
            )

class FinalResults(Page):
    def is_displayed(self):
        return self.player.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):

        return dict(
            earning = self.player.payoff - c(5),
            show_up_fee = c(5),
            payoff = self.player.payoff
            )


page_sequence = [Welcome, 
                SetupWaitPage,
                VotingStage1,
                VotingStage1WaitPage,
                VotingStage2,
                ResultsWaitPage,
                Results,
                FinalResults
                ]