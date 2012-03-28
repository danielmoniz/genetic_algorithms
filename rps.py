from rps_organism import SubOrganism as Organism
import utility
from random import random
import math

class RockPaperScissors():
    def __init__(self, population, num_game_turns):
        self.name = "Rock, Paper, Scissors"
        self.population = population 
        self.num_game_turns = num_game_turns 
        self.actions = ['R', 'P', 'S']

    def generate_initial_population(self):
        """Generate the initial population of AI strategies. Do so completely
        randomly."""
        return [Organism(self.create_random_rps_tuple()) for i in range(self.population)]

    def create_random_rps_tuple(self):
        """Generate a random RPS probability distribution. Returns a normalized
        tuple."""
        num_actions = len(self.actions)
        return utility.normalize_tuple(
            tuple([random() for j in range(num_actions)]))

    def get_rps_choice(self, rps_distribution):
        """Return a random choice given a probability distribution between R, P,
        and S."""
        random_choice = random()
        index_choice = utility.get_distribution_choice(rps_distribution)
        return self.actions[index_choice]

    def get_rps_dist_game_results(self, rps_distributions, opponent_input):
        """Return the RPS distribution game results. Run the opponent's input
        against all of the given AI scripts (rock-paper-scissors distributions,
        stored as tuples)."""
# determine choice of R, P, or S given each RPS probability distribution
        ai_choices = [self.get_rps_choice(rps_dist) for rps_dist in rps_distributions]

        return [self.run_game_logic(ai_choice, opponent_input) for ai_choice in ai_choices]

    def run_game_turn(self, organisms, opponent_input):
        """Run a game turn given RPS distributions and an opponent's input.
        Then kill the weak members and generate new ones. Return a list of the
        remaining organisms."""
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

# Kill the least-performing organisms.
        num_members_to_breed = self.kill_worst_organisms(organisms)

# Breed new organisms to fill thhe gap caused by killing them.
        if num_members_to_breed > 0:
            for i in range(num_members_to_breed):
# Note that choice() is a function from the random module
                best_parents = self.get_strongest_organisms(organisms)
                member_to_breed = self.breed_organism_from_parents(best_parents)
                organisms.append(member_to_breed.reproduce())
            
        return organisms

    def kill_worst_organisms(self, organisms):
        """Finds the least-performing organisms and kills them. Returns the
        number of killed organisms. Does NOT return a set of organisms; it
        simply removes them from the list sent as a parameter."""
# Find all organisms with at least X turns played. These can be killed.
        is_killable = lambda org:len(org.recent_turn_results) >= org.num_turns_stored
        killable_organisms = filter(is_killable, organisms)

# order the organisms by their success value
        ordered_organisms = sorted(killable_organisms, key=lambda org:org.get_success_value())

# Generate success values for each organisms' recent track record.
        success_values = [org.get_success_value() for org in killable_organisms]
# calculate how many organisms should be killed (and bred). Should be the
# number of killable organisms divided by two (rounded up)
        num_members_to_breed = int(math.ceil(float(len(ordered_organisms))/2))

# finally, remove organisms and return number killed/number to breed.
        for i in range(num_members_to_breed):
            organisms.remove(ordered_organisms[i])
        return num_members_to_breed

# DEPRECATED
    def kill_worst_organisms_by_hit_points(self, organisms):
        """Unused, but still useable. Kills worst organisms based on their
        reaching 0 hit points. Returns the number of organisms killed."""
        for organism in organisms:
            if organism.hit_points <= 0:
                organisms.remove(organism)

# calculate number of organisms to breed and return this number
        num_members_to_breed = self.population - len(organisms)
        return num_members_to_breed

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
