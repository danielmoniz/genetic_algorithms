import math
from random import random
from random import choice

POPULATION = 100

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

# store losses and wins (store wins for kicks)
        self.losses = 0
        self.wins = 0

    def reproduce(self):
        """Each chromosone reproduces asexually."""
        if random() < self.potency:
            pass
# be like parent
            return Chromosone(self.rps, self.mutation_tendency, self.potency)
        else:
            pass
# be different from parent
            return Chromosone(self.rps, self.mutation_tendency, self.potency)


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
        """rps_tuple = []
        for j in range(3):
            rps_tuple.append(random())
        rps_tuple = tuple(rps_tuple)"""
        rps_tuple = tuple([random() for j in range(3)])
        rps_tuple = normalize_tuple(rps_tuple)
        chromosones.append(Chromosone(rps_tuple))

    # one line solution
    # chromosones = [Chromosone(tuple([random() for j in range(3)])) for i in range(POPULATION)]

    return chromosones

def get_rps_dist_game_results(rps_distributions, opponent_input):
    """Return the RPS distribution game results. Run the opponent's input
    against all of the given AI scripts (rock-paper-scissors distributions,
    stored as tuples)."""
    ai_choices = [get_rps_choice(rps_dist) for rps_dist in rps_distributions]
# determine choice of R, P, or S given each RPS probability distribution

    return [run_game_logic(ai_choice, opponent_input) for ai_choice in ai_choices]

def get_rps_choice(rps_distribution):
    """Return a random choice given a probability distribution between R, P, and S."""
    random_choice = random()
# @TODO rps should be defined externally somewhere
    rps = ['R', 'P', 'S']
    rps_choice = None
    for i in range(len(rps_distribution)):
        interval = sum(rps_distribution[0:i+1])
        if random_choice <= interval:
            rps_choice = rps[i]
            break
    return rps_choice

def run_game_turn(chromosones, opponent_input):
    """Run a game turn given RPS distributions and an opponent's input. Then kill the weak members and generate new ones."""
    rps_distributions = [chrom.rps for chrom in chromosones]
    turn_results = get_rps_dist_game_results(rps_distributions, opponent_input)
# if there is a win in the population, kill non-winners and re-populate with
# children of winners
    winners = []
    if 'win' in turn_results:
        for i in range(len(turn_results)):
            if (turn_results[i] == 'win'):
                winners.append(chromosones[i])
    # @TODO NEED to account for cases where none of the population win (or tie)
    else:
# quick hack: grab two random chromosones if nobody wins
# @TODO Fix this! Should be pulling the chromosones that tie, rather than win
        winners = [choice(chromosones) for i in range(2)]

# Breed new chromosones, equal to the number of open spaces left in the
# controlled population. Select randomly from the list of winners.
    num_members_to_breed = POPULATION - len(winners)
    for i in range(num_members_to_breed):
# Note that choice() is a function from the random module
        member_to_breed = choice(winners)
        winners.append(member_to_breed.reproduce())
    for chrom in winners:
        print [round(rps_element, 2) for rps_element in chrom.rps]
    print "-----------------------------------"
        
    # print [chrom.rps for chrom in winners]

# if there are no ties and no wins, don't kill any of the organisms

def run_game_logic(input1, input2):
    """Assumes input has been cleaned and formatted to fit 'R', 'P', or 'S' for
    Rock, Paper, and Scissors.  Runs the game on the given inputs.
    Returns 'win', 'lose', or 'draw', centered on input1 as the main player."""
    if input1 == input2:
        return 'draw'
    elif input1 == 'R':
        if input2 == 'P':
            return 'lose'
        elif input2 == 'S':
            return 'win'
# should not hit else! input1==input2 case already covered
    elif input1 == 'P':
        if input2 == 'R':
            return 'win'
        elif input2 == 'S':
            return 'lose'
# should not hit else! input1==input2 case already covered
    elif input1 == 'S':
        if input2 == 'R':
            return 'lose'
        elif input2 == 'P':
            return 'win'
    else:
        print "Something went hideously wrong in the game_logic function."
        exit(0)


chromosones = generate_initial_population()
# print chromosones 
for chrom in chromosones:
    """print chrom.rps
    print chrom.mutation_tendency
    print chrom.potency"""

for i in range(100):
    run_game_turn(chromosones, 'R')
