import sys
from utility import normalize_tuple
from random import random
from random import choice
from rps_organism import SubOrganism as Organism

print "------------------------"
try:
    POPULATION = int(sys.argv[1])
    NUM_GAME_TURNS = int(sys.argv[2])
    print "Population:", POPULATION, ", number of game turns:", NUM_GAME_TURNS
except IndexError:
# Default population and game turn settings
    POPULATION = 100
    NUM_GAME_TURNS = 20
    print "Using default population (" + str(POPULATION) + ") and number of game turns (" + str(NUM_GAME_TURNS) + ")."

def generate_initial_population():
    """Generate the initial population of AI strategies. Do so completely
    randomly."""
    return [Organism(create_random_rps_tuple()) for i in range(POPULATION)]

def create_random_rps_tuple():
    """Generate a random RPS probability distribution. Returns a normalized
    tuple."""
# @TODO Deal with magic number 3 !
    return normalize_tuple(tuple([random() for j in range(3)]))

def get_rps_dist_game_results(rps_distributions, opponent_input):
    """Return the RPS distribution game results. Run the opponent's input
    against all of the given AI scripts (rock-paper-scissors distributions,
    stored as tuples)."""
    ai_choices = [get_rps_choice(rps_dist) for rps_dist in rps_distributions]
# determine choice of R, P, or S given each RPS probability distribution

    return [run_game_logic(ai_choice, opponent_input) for ai_choice in ai_choices]

def get_rps_choice(rps_distribution):
    """Return a random choice given a probability distribution between R, P,
    and S."""
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
    for org in organisms:
        print dir(org)
        print "turns in play:", org.turns
    print "==="
    #print organisms
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
            best_parents = get_strongest_organisms(organisms)
            member_to_breed = breed_organism_from_parents(best_parents)
            organisms.append(member_to_breed.reproduce())

    """for chrom in organisms:
        print [round(rps_element, 2) for rps_element in chrom.rps],
        print "Hit points:", chrom.hit_points
    print "-----------------------------------"
    """
        
    return organisms

def get_strongest_organisms(organisms):
    """Return a list of the strongest organisms. Will be at least one, but could be more."""
    strongest_value = 0
    strongest = []
    for organism in organisms:
        if organism.hit_points >= strongest_value:
# empty the list of strongest organisms if a stronger one shows up
            if organism.hit_points > strongest_value:
                del strongest[:]
                strongest_value = organism.hit_points
            strongest.append(organism)

    return strongest

def breed_organism_from_parents(organisms):
    """Given a list of organisms, return a child of all of them by averaging their rps distributions."""
    rps_distributions = [org.rps for org in organisms]
    rps_collection = zip(*rps_distributions)
    new_rps_tuple = tuple([sum(collection)/len(collection) for collection in rps_collection])

# generate new mutation_tendency and potency based on the top organisms
    mutation_tendencies = [org.mutation_tendency for org in organisms]
    new_mutation_tendency = sum(mutation_tendencies)/len(mutation_tendencies)
    potencies = [org.potency for org in organisms]
    new_potency = sum(mutation_tendencies)/len(mutation_tendencies)

    return Organism(new_rps_tuple, new_mutation_tendency, new_potency)

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

print "---------------------------------------------------"
chromosones = generate_initial_population()
for chrom in chromosones:
    print chrom
    print chrom.rps

organisms = []
for i in range(NUM_GAME_TURNS):
    organisms = run_game_turn(chromosones, 'R')

#print get_organism_stats(organisms)
organism_list = []
for chrom in organisms:
    organism_list.append([chrom.hit_points, [round(rps_element, 2) for rps_element in chrom.rps]])

organism_list = sorted(organism_list)
print "Top 5 (or less) organisms, sorted by hit points:"
for org in reversed(organism_list[-5:]):
    print org

strongest_organisms = get_strongest_organisms(organisms)

super_child_organism = breed_organism_from_parents(strongest_organisms)
print "Latest super child organism:", [round(rps_element, 2) for rps_element in super_child_organism.rps]
