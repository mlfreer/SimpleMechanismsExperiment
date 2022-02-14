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
        if values['question']!=Constants.a11:
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
        if values['question']!=Constants.a12:
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

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

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

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

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

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

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

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

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

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

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

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

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

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a25:
            return 'error'
#-----------------------------------------------------------------------------------




#-----------------------------------------------------------------------------------
# BLOCK 3 [SOB STAGE 1]:
class Question31(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.SecondOrder

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']-2
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a31:
            return 'error'

class Question32(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.SecondOrder

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']-2
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a32:
            return 'error'

class Question33(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.SecondOrder

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']-2
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a33:
            return 'error'

class Question34(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.SecondOrder

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']-2
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a34:
            return 'error'
#-----------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------
# BLOCK 4 [SOB STAGE 2]:
class Question41(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.FirstOrder

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']-1
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a41:
            return 'error'

class Question42(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.FirstOrder

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']-1
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a42:
            return 'error'

class Question43(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.FirstOrder

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']-1
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a43:
            return 'error'
#-----------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------
# BLOCK 5 [SOB STAGE 3]:
class Question51(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.DominantStrategy

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a51:
            return 'error'



class Question52(Page):
    def is_displayed(self):
        return self.session.config['treatment'] >= Constants.DominantStrategy

    form_model  = 'player'
    form_fields = ['question']

    def vars_for_template(self):
        temp = self.session.config['treatment']
        return dict(
            stage_number = temp,
            )

    form_show_errors = False

    def before_next_page(self):
        self.player.question_number = self.player.question_number+1

    def error_message(player, values):
        if values['question']!=Constants.a52:
            return 'error'
#-----------------------------------------------------------------------------------




page_sequence = [
            Welcome,
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
            # block 3:
#            Question31,
#            Question32,
#            Question33,
#            Question34,
            # block 4:
#            Question41,
#            Question42,
#            Question43,
            # block 5:
#            Question51,
#            Question52
            ]
