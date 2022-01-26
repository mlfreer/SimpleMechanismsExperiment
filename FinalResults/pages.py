from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants





# page with final results:
class FinalResults(Page):
    def vars_for_template(self):
        return dict(
            earning = c(p.earnings),
            show_up_fee = c(5),
            beauty_contest  = c(self.player.bc_earnings),
            risk = c(self.player.risk_earnings),
            payoff = self.player.payoff
            )


page_sequence = [
                # final results
                FinalResults
]
