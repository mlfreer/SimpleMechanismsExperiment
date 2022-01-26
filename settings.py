from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    # dict(
    #    name='public_goods',
    #    display_name="Public Goods",
    #    num_demo_participants=3,
    #    app_sequence=['public_goods', 'payment_info']
    # ),
    {
         'name': 'DSVotingU',
         'display_name': 'Dominant Strategy Voting with Unequal Strategy Space',
         'num_demo_participants': 4,
         'app_sequence': ['DSVotingU'],
     },
     {
         'name': 'FOBVotingU',
         'display_name': 'First Order Beliefs Voting with Unequal Strategy Space',
         'num_demo_participants': 4,
         'app_sequence': ['FOBVotingU'],
     },
     {
         'name': 'SOBVotingU',
         'display_name': 'Second Order Beliefs Voting with Unequal Strategy Space',
         'num_demo_participants': 4,
         'app_sequence': ['SOBVotingU'],
     },
     {
         'name': 'BeautyContest',
         'display_name': 'Beauty Contest',
         'num_demo_participants': 2,
         'app_sequence': ['BeautyContest'],
     },
     {
         'name': 'RiskElicitation',
         'display_name': 'Risk Elicitation Task',
         'num_demo_participants': 1,
         'app_sequence': ['RiskElicitation'],
     },
     {
         'name': 'PostExperimentalTasks',
         'display_name': 'Post Experimental Tasks (both Beauty Contest and Risk Elictiation)',
         'num_demo_participants': 2,
         'app_sequence': ['BeautyContest','RiskElicitation'],
     },

]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'zo6w*31z6&i%#fo9)jdr88a^-z7p&*^u%_gr26n67*=jsbn=xe'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
