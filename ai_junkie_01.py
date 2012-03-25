from random import random
number_to_solve = 50
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.001
POP_SIZE = 100

# 4 bits determine each piece of information
GENE_LENGTH = 4
CHROMO_LENGTH = 300

def generate_random_population():
    # rand_int = randint(8, 20)
    # print rand_int
    print getrandbits(CHROMO_LENGTH)
    
generate_random_population()
