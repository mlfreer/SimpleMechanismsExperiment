from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants





# page with final results:
class FinalResults(Page):
    def vars_for_template(self):
        return dict(
            treatment_earnings = c(self.player.participant.vars['treatment_earnings']),
            bc_earnings = c(self.player.participant.vars['bc_earnings']),
            risk_earnings = c(self.player.participant.vars['risk_earnings']),
            total_earnings = c(self.player.participant.vars['treatment_earnings'])+c(self.player.participant.vars['bc_earnings'])+c(self.player.participant.vars['risk_earnings']),
            show_up_fee = self.session.config['participation_fee'],
            code = self.player.participant.code
            )


page_sequence = [
                # final results
                FinalResults
]
