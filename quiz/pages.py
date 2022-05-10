from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


#-----------------------------------------------------------------------------------
# welcome page:
class Welcome(Page):
    pass
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# BLOCK 1 [first table]:
class Question1(Page):
    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        print(self.session.config['treatment']==1)
        return dict(
            my_number = 1,
            my_profile = 0,
            my_preferences = Constants.preferences[0],
            preference_profiles = Constants.preferences
            )

    form_show_errors = False

    def error_message(player, values):
        if values['question']!=Constants.a1:
            return 'error'

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1


class Question2(Page):
    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        return dict(
            my_number = 1,
            my_profile = 0,
            my_preferences = Constants.preferences[0],
            preference_profiles = Constants.preferences
            )

    form_show_errors = False

    def error_message(player, values):
        if values['question']!=Constants.a2:
            return 'error'

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1


class Question3(Page):
    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        return dict(
            my_number = 1,
            my_profile = 0,
            my_preferences = Constants.preferences[0],
            preference_profiles = Constants.preferences
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a3:
            return 'error'
#-----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------
class Question4(Page):
    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        return dict(
            my_number = 2,
            my_profile = 2,
            my_preferences = Constants.preferences[2],
            preference_profiles = Constants.preferences
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a4:
            return 'error'


class Question5(Page):
    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        return dict(
            my_number = 2,
            my_profile = 2,
            my_preferences = Constants.preferences[2],
            preference_profiles = Constants.preferences
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a5:
            return 'error'

class Question6(Page):
    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        return dict(
            my_number = 2,
            my_profile = 2,
            my_preferences = Constants.preferences[2],
            preference_profiles = Constants.preferences
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a6:
            return 'error'



page_sequence = [
            Welcome,
            # block 1:
            Question1,
            Question2,
            Question3,
            # block 2:
            Question4,
            Question5, 
            Question6,
            ]
