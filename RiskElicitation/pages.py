from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


# risk elicitation instructions:
class RiskElicitationInstructions(Page):
    def vars_for_template(self):
        return dict(
            high_payoff = Constants.risk_max,
            low_payoff = Constants.risk_min,
            safe_payoff = Constants.risk_safe,
            payment_probability = Constants.risk_prob_paying*100,
            )


class RiskElicitationDecision(Page):
    form_model = 'player'
    form_fields = ['risk_choice']

    def vars_for_template(self):
        return dict(
            high_payoff = Constants.risk_max,
            low_payoff = Constants.risk_min,
            safe_payoff = Constants.risk_safe,
            payment_probability = Constants.risk_prob_paying*100,
            )

class RiskElicitationWaitPage(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        players = self.subsession.get_players()
        for p in players:
            p.set_risk_results()
            p.participant.vars['risk_earnings'] = p.risk_earnings

# temporary results page
class RiskElicitationResults(Page):
    def vars_for_template(self):
        print(self.player.participant.vars)
        return dict(
            risk_earning = self.player.risk_earnings,
            bc_earning = self.player.participant.vars['bc_earnings'],
            choice = self.player.risk_choice,
            )

page_sequence = [
                # risk elicitation task
                RiskElicitationInstructions,
                RiskElicitationDecision,
                RiskElicitationWaitPage,
#                RiskElicitationResults
]
