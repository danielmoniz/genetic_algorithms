import math
from random import random

POPULATION = 10

class Chromosone():
    """Stores information about chromosone objects such as their chances of mutation, similarity to offspring, etc."""
    
    def __init__(self, rps, mutation_tendency = 0.01, potency = 0.5):
        """Potency determines the similarity to the parent when reproducing.
        Mutation tendency determines, when a child is different, how different
        it is.
        'rps' is the tuple indication the distribution of rock, paper, and
        scissors in a strategy."""
# use parent's mutation tendency to determine all mutations for child
        self.mutation_tendency = post_mutation_value(mutation_tendency, mutation_tendency)
        self.potency = post_mutation_value(mutation_tendency, potency)

# calculate the new tuple indicating the chromosone's RPS strategy
        rps_tuple = tuple([post_mutation_value(mutation_tendency, i) for i in rps]) 
        self.rps = normalize_tuple(rps_tuple)

    def reproduce(self):
        """Each chromosone reproduces asexually."""
        if random() < self.potency:
            pass
# be like parent
            return Chromosone(self.mutation_tendency, self.potency)
        else:
            pass
# be different from parent


def normalize_tuple(tuple_to_normalize, total = 1):
    """Take a total value and a tuple. Normalize the tuple's entries such that
    they add up to total."""
    if total == 0:
        return False
    current_total = sum(tuple_to_normalize)
    divisor = current_total / total
    return tuple([i/divisor for i in tuple_to_normalize])

def post_mutation_value(tendency, current_value):
    """Determine the value after a mutation given the mutation tendency and the
    original value itself."""
    if random() <= tendency:
        sign = lambda x: math.copysign(1, x)
        mod_sign = sign(random() - 0.5)
        mutation_value = (mod_sign * tendency) * current_value
    else:
        mutation_value = 0

    return current_value + mutation_value

def generate_initial_population():
    """Generate the initial population of AI strategies. Do so completely
    randomly."""
    chromosones = []
    for i in range(POPULATION):
# create random RPS tuple
        rps_tuple = tuple([random() for j in range(3)])
        rps_tuple = normalize_tuple(rps_tuple)
        chromosones.append(Chromosone(rps_tuple))

    return chromosones


chromosones = generate_initial_population()
for chrom in chromosones:
    print chrom.rps
    print chrom.mutation_tendency
    print chrom.potency
