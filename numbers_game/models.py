from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from numpy.random import uniform
from otree.db.models import Model, ForeignKey
from django.db.models.deletion import CASCADE
import random

author = 'Daniel'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'numbers_game'
    players_per_group = None
    num_rounds = 1
    endowment = c(10)
    min_number = c(0)
    max_number = c(20)


class Subsession(BaseSubsession):
    def before_session_starts(self):  # called each round
        """For each player, create a fixed number of "decision stubs" with random values to be decided upon later."""
        for p in self.get_players():
            # p.generate_decision_stubs()
            p.assigned_number = uniform(Constants.min_number, Constants.max_number)


class Group(BaseGroup):
    group_policy = models.FloatField()

    def set_payoffs(self):
        for p in self.get_players():
            p.payoff = abs(p.chosen_number - self.group_policy)


class Player(BasePlayer):
    assigned_number = models.IntegerField()
    chosen_number = models.IntegerField()

    # def generate_decision_stubs(self):
    #     """
    #     Create a fixed number of "decision stubs", i.e. decision objects that only have a random "value" field on
    #     which the player will base her or his decision later in the game.
    #     """
    #     decision = self.decision_set.create()  # create a new Decision object as part of the player's decision set
    #     decision.value = random.randint(1, 10)  # don't forget to "import random" before!
    #     decision.save()  # important: save to DB!


# class Decision(Model):  # our custom model inherits from Django's base class "Model"
#     chosen_number = models.IntegerField()
#     player_decided = models.BooleanField()
#     round_id = models.IntegerField()
#     player = ForeignKey(Player, on_delete=CASCADE)  # creates 1:m relation -> this decision was made by a certain player

