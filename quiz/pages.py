from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


#-----------------------------------------------------------------------------------
# BLOCK 1 [first table]:
class Question1(Page):
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
        if values['question']!=Constants.a11:
            return 'error'


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
        if values['question']!=Constants.a12:
            return 'error'


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

    def error_message(player, values):
        if values['question']!=Constants.a13:
            return 'error'

class Question4(Page):
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
        if values['question']!=Constants.a14:
            return 'error'


class Question5(Page):
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
        if values['question']!=Constants.a14:
            return 'error'
#-----------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------
# BLOCK 2 [second table]:
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

    def error_message(player, values):
        if values['question']!=Constants.a21:
            return 'error'

class Question7(Page):
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

    def error_message(player, values):
        if values['question']!=Constants.a22:
            return 'error'


class Question8(Page):
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

    def error_message(player, values):
        if values['question']!=Constants.a23:
            return 'error'

class Question9(Page):
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

    def error_message(player, values):
        if values['question']!=Constants.a24:
            return 'error'

class Question10(Page):
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

    def error_message(player, values):
        if values['question']!=Constants.a25:
            return 'error'
#-----------------------------------------------------------------------------------

page_sequence = [
            # block 1:
            Question1,
            Question2,
            Question3,
            Question4,
            Question5,
            # block 2:
            Question6,
            Question7,
            Question8,
            Question9,
            Question10,
            ]
