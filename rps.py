import math
from random import random
from random import choice

POPULATION = 100
HIT_POINTS = 10

class Chromosone():
    """Stores information about chromosone objects such as their chances of mutation, similarity to offspring, etc."""
    
    def __init__(self, rps, mutation_tendency = 0.1, potency = 0.5):
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
        self.draws = 0
        self.hit_points = HIT_POINTS

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

    def lose(self):
        self.losses += 1
        self.hit_points -= 3

    def win(self):
        self.wins += 1
        self.hit_points += 1

    def draw(self):
        self.draws += 1
        self.hit_points -= 1

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

def run_game_turn(organisms, opponent_input):
    """Run a game turn given RPS distributions and an opponent's input. Then kill the weak members and generate new ones."""
    rps_distributions = [chrom.rps for chrom in organisms]
    turn_results = get_rps_dist_game_results(rps_distributions, opponent_input)

# store wins and losses in each organism
    for i in range(len(organisms)):
        if turn_results[i] == 'win':
            organisms[i].win()
        elif turn_results[i] == 'draw':
            organisms[i].draw()
        elif turn_results[i] == 'loss':
            organisms[i].lose()

# if organism has run out of hit points, kill it!
    for organism in organisms:
        if organism.hit_points <= 0:
            organisms.remove(organism)

        

# Breed new organisms, equal to the number of open spaces left in the
# controlled population. Select randomly from the list of organisms.
    num_members_to_breed = POPULATION - len(organisms)
    if num_members_to_breed > 0:
        for i in range(num_members_to_breed):
# Note that choice() is a function from the random module
            member_to_breed = choice(organisms)
            organisms.append(member_to_breed.reproduce())

    """for chrom in organisms:
        print [round(rps_element, 2) for rps_element in chrom.rps],
        print "Hit points:", chrom.hit_points
    print "-----------------------------------"
    """
        
    return organisms


def run_game_logic(input1, input2):
    """Assumes input has been cleaned and formatted to fit 'R', 'P', or 'S' for
    Rock, Paper, and Scissors.  Runs the game on the given inputs.
    Returns 'win', 'lose', or 'draw', centered on input1 as the main player."""
    if input1 == input2:
        return 'draw'
    elif input1 == 'R':
        if input2 == 'P':
            return 'loss'
        elif input2 == 'S':
            return 'win'
# should not hit else! input1==input2 case already covered
    elif input1 == 'P':
        if input2 == 'R':
            return 'win'
        elif input2 == 'S':
            return 'loss'
# should not hit else! input1==input2 case already covered
    elif input1 == 'S':
        if input2 == 'R':
            return 'loss'
        elif input2 == 'P':
            return 'win'
    else:
        print "Something went hideously wrong in the game_logic function."
        exit(0)

"""def get_organism_stats(organisms):
    organism_rps_sum = []
    for organism in organisms:
        organism"""
        
chromosones = generate_initial_population()

organisms = []
for i in range(1000):
    organisms = run_game_turn(chromosones, 'R')

#print get_organism_stats(organisms)
organism_list = []
for chrom in organisms:
    organism_list.append([chrom.hit_points, [round(rps_element, 2) for rps_element in chrom.rps]])
    """print [round(rps_element, 2) for rps_element in chrom.rps],
    print "Hit points:", chrom.hit_points"""

organism_list = sorted(organism_list)
for org in organism_list:
    print org

"""
# if there is a win in the population, kill non-winners and re-populate with
# children of winners
    winners = []
    if 'win' in turn_results:
        for i in range(len(turn_results)):
            if (turn_results[i] == 'win'):
                winners.append(organisms[i])
    # @TODO NEED to account for cases where none of the population win (or tie)
    else:
# quick hack: grab two random organisms if nobody wins
# @TODO Fix this! Should be pulling the organisms that tie, rather than win
        winners = [choice(organisms) for i in range(2)]"""
