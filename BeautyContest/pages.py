from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# beauty contest task
class BeautyContestInstructions(Page):
    pass
    
class BeautyContestDecision(Page):
    form_model = 'player'
    form_fields = ['bc_guess']


class BeautyContestWaitPage(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.set_bc_results()

# for testing purposes
class BeautyContestResults(Page):
    def vars_for_template(self):
        return dict(
            earning = self.player.bc_earnings,
            guess = self.player.bc_guess
            )

page_sequence = [# beuaty contest task
                BeautyContestInstructions,
                BeautyContestDecision,
                BeautyContestWaitPage,
                BeautyContestResults
                ]
