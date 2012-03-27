from utility import normalize_tuple
import math
from random import random

HIT_POINTS = 10

class Organism():
    """Stores information about chromosone objects such as their chances of
    mutation, similarity to offspring, etc."""
    
    def __init__(self, mutation_tendency = 0.1, potency = 0.5):
        """Potency determines the similarity to the parent when reproducing.
        Mutation tendency determines, when a child is different, how different
        it is. 'rps' is the tuple indication the distribution of rock, paper,
        and scissors in a strategy."""
# use parent's mutation tendency to determine all mutations for child
        self.mutation_tendency = self.post_mutation_value(mutation_tendency,
            mutation_tendency)
        self.potency = self.post_mutation_value(mutation_tendency, potency)

# store losses and wins (store wins for kicks)
        self.losses = 0
        self.wins = 0
        self.draws = 0
        self.turns = 0
        self.hit_points = HIT_POINTS
        self.num_turns_stored = 5
        self.recent_turn_results = []

    def lose(self):
        """Tells the organism that it lost a round of play."""
        self.losses += 1
        self.hit_points -= 3
        self.turns += 1
        self.update_recent_turn_results('L')

    def win(self):
        """Tells the organism that it won a round of play."""
        self.wins += 1
        self.hit_points += 1
        self.turns += 1
        self.update_recent_turn_results('W')

    def draw(self):
        """Tells the organism that it tied in a round of play."""
        self.draws += 1
        self.hit_points -= 1
        self.turns += 1
        self.update_recent_turn_results('D')

    def update_recent_turn_results(self, result):
        """Update the object attribute storing the previous X turns of data.
        Ensure that there is never more than X pieces of data stored."""
        if len(self.recent_turn_results) >= self.num_turns_stored:
            self.recent_turn_results.pop(0)
        self.recent_turn_results.append(result)

    def get_success_value(self):
        """Returns a value indication the overall effectiveness of the
        organism."""
        pass

    def post_mutation_value(self, tendency, current_value):
        """Determine the value after a mutation given the mutation tendency and
        the original value itself."""
        if random() <= tendency:
            sign = lambda x: math.copysign(1, x)
            mod_sign = sign(random() - 0.5)
            mutation_value = (mod_sign * tendency) * current_value
        else:
            mutation_value = 0

        return current_value + mutation_value

    def reproduce(self):
        """Each chromosone reproduces asexually."""
        if random() < self.potency:
            pass
# be like parent
            return Organism(self.mutation_tendency, self.potency)
        else:
            pass
# be different from parent
            return Organism(self.mutation_tendency, self.potency)
