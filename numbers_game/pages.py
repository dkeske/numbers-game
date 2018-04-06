from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.forms import modelformset_factory


class WelcomePage(Page):
    form_model = 'player'
    form_fields = ['chosen_number']

    # DecisionFormSet = modelformset_factory(Decision, fields=('chosen_number', 'round_number'), extra=0)


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    WelcomePage,
    ResultsWaitPage,
    Results
]
