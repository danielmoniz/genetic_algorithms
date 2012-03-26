from utility import normalize_tuple
from organism import Organism

class SubOrganism(Organism):
    def __init__(self, rps, mutation_tendency = 0.1, potency = 0.5):
        Organism.__init__(self, rps, mutation_tendency, potency)

# calculate the new tuple indicating the chromosone's RPS strategy
        rps_tuple = tuple([self.post_mutation_value(mutation_tendency, i) for i
            in rps]) 
        self.rps = normalize_tuple(rps_tuple)

