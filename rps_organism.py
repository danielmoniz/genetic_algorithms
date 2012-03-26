from utility import normalize_tuple
from organism import Organism
from random import random

class SubOrganism(Organism):
    def __init__(self, rps, mutation_tendency = 0.1, potency = 0.5):
        Organism.__init__(self, mutation_tendency, potency)

# calculate the new tuple indicating the chromosone's RPS strategy
        rps_tuple = tuple([self.post_mutation_value(mutation_tendency, i) for i
            in rps]) 
        print "in constructor. rps:", rps_tuple
        self.rps = normalize_tuple(rps_tuple)

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
