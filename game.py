from rps_organism import SubOrganism as Organism
from utility import normalize_tuple
from random import random

class RockPaperScissors():
    def __init__(self, population, num_game_turns):
        self.name = "Rock, Paper, Scissors"
        self.population = population 
        self.num_game_turns = num_game_turns 

    def generate_initial_population(self):
        """Generate the initial population of AI strategies. Do so completely
        randomly."""
        return [Organism(self.create_random_rps_tuple()) for i in range(self.population)]

    def create_random_rps_tuple(self):
        """Generate a random RPS probability distribution. Returns a normalized
        tuple."""
# @TODO Deal with magic number 3 !
        return normalize_tuple(tuple([random() for j in range(3)]))

    def get_rps_choice(self, rps_distribution):
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

    def get_rps_dist_game_results(self, rps_distributions, opponent_input):
        """Return the RPS distribution game results. Run the opponent's input
        against all of the given AI scripts (rock-paper-scissors distributions,
        stored as tuples)."""
        ai_choices = [self.get_rps_choice(rps_dist) for rps_dist in rps_distributions]
# determine choice of R, P, or S given each RPS probability distribution

        return [self.run_game_logic(ai_choice, opponent_input) for ai_choice in ai_choices]

    def run_game_turn(self, organisms, opponent_input):
        """Run a game turn given RPS distributions and an opponent's input. Then kill the weak members and generate new ones."""
        rps_distributions = [chrom.rps for chrom in organisms]

        turn_results = self.get_rps_dist_game_results(rps_distributions, opponent_input)

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
        num_members_to_breed = self.population - len(organisms)
        if num_members_to_breed > 0:
            for i in range(num_members_to_breed):
# Note that choice() is a function from the random module
                best_parents = self.get_strongest_organisms(organisms)
                member_to_breed = self.breed_organism_from_parents(best_parents)
                organisms.append(member_to_breed.reproduce())
            
        return organisms

# @TODO Could use unit testing for the run_game_logic function.
    def run_game_logic(self, input1, input2):
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

    def breed_organism_from_parents(self, organisms):
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

    def get_strongest_organisms(self, organisms):
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

