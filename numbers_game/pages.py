from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.forms import modelformset_factory
from numpy import mean


class WelcomePage(Page):
    form_model = 'player'
    form_fields = ['chosen_number']

    # DecisionFormSet = modelformset_factory(Decision, fields=('chosen_number', 'round_number'), extra=0)


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        group_players = self.group.get_players()
        group_numbers = [p.chosen_number for p in group_players]
        self.group.group_policy = mean(group_numbers)
        if self.group.round_number == Constants.num_rounds:
            self.group.set_payoffs()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        player_in_all_rounds = self.player.in_all_rounds()

        return {
            'player_in_all_rounds': player_in_all_rounds,
        }


page_sequence = [
    WelcomePage,
    ResultsWaitPage,
    Results
]
