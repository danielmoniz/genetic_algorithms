from utility import normalize_tuple
import math
from random import random

HIT_POINTS = 10

class Organism():
    """Stores information about chromosone objects such as their chances of
    mutation, similarity to offspring, etc."""
    
    def __init__(self, rps, mutation_tendency = 0.1, potency = 0.5):
        """Potency determines the similarity to the parent when reproducing.
        Mutation tendency determines, when a child is different, how different
        it is. 'rps' is the tuple indication the distribution of rock, paper,
        and scissors in a strategy."""
# use parent's mutation tendency to determine all mutations for child
        self.mutation_tendency = self.post_mutation_value(mutation_tendency,
            mutation_tendency)
        self.potency = self.post_mutation_value(mutation_tendency, potency)

# calculate the new tuple indicating the chromosone's RPS strategy
        rps_tuple = tuple([self.post_mutation_value(mutation_tendency, i) for i in rps]) 
        self.rps = normalize_tuple(rps_tuple)

# store losses and wins (store wins for kicks)
        self.losses = 0
        self.wins = 0
        self.draws = 0
        self.hit_points = HIT_POINTS

    def reproduce(self):
        """Each chromosone reproduces asexually."""
        if random() < self.potency:
            pass
# be like parent
            return Organism(self.rps, self.mutation_tendency, self.potency)
        else:
            pass
# be different from parent
            return Organism(self.rps, self.mutation_tendency, self.potency)

    def lose(self):
        self.losses += 1
        self.hit_points -= 3

    def win(self):
        self.wins += 1
        self.hit_points += 1

    def draw(self):
        self.draws += 1
        self.hit_points -= 1

    def post_mutation_value(self, tendency, current_value):
        """Determine the value after a mutation given the mutation tendency and the
        original value itself."""
        if random() <= tendency:
            sign = lambda x: math.copysign(1, x)
            mod_sign = sign(random() - 0.5)
            mutation_value = (mod_sign * tendency) * current_value
        else:
            mutation_value = 0

        return current_value + mutation_value

