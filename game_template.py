from your_suborganism_class import SubOrganism as Organism
import utility
from random import random

class YourGameName():
    def __init__(self, population, num_game_turns):
        self.name = "Your Game Name"
        self.population = population 
        self.num_game_turns = num_game_turns 
        self.actions = ['list of available actions as strings']

    def generate_initial_population(self):
        """Generate the initial population of AI strategies. Do so completely
        randomly. Return a list of generated organisms."""
        pass

    def create_random_rps_tuple(self):
        """Generate a random YourGameName probability distribution. Uses the
        utility class to return a normalized tuple."""
        pass

    def get_rps_choice(self, rps_distribution):
        """Return a random choice given a probability distribution between the
        available actions."""
# This has been left in simply because it hardly needs to be changed. Modify
# the variable names to fit your game.
        random_choice = random()
        index_choice = utility.get_distribution_choice(rps_distribution)
        return self.actions[index_choice]

    def get_rps_dist_game_results(self, rps_distributions, opponent_input):
        """Return the action distribution game results, ie. a list of turn
        outcomes as strings. Run the opponent's input against all of the given
        AI scripts (eg. rock-paper-scissors distributions, stored as tuples)."""
        pass

    def run_game_turn(self, organisms, opponent_input):
        """Run a game turn given action distributions and an opponent's input.
        Then kill the weak members and generate new ones. Return a list of the
        remaining organisms."""
        pass

    def kill_worst_organisms(self, organisms):
        """Finds the least-performing organisms and kills them. Returns the
        number of killed organisms. Does NOT return a set of organisms; it
        simply removes them from the list sent as a parameter."""
        pass

# DEPRECATED
    def kill_worst_organisms_by_hit_points(self, organisms):
        """Unused, but still useable. Kills worst organisms based on their
        reaching 0 hit points. Returns the number of organisms killed."""
        pass

    def run_game_logic(self, input1, input2):
        """Assumes input has been cleaned and formatted to fit actions for the
        give game (eg. 'R', 'P', 'S').  Runs the game on the given inputs.
        Returns 'win', 'lose', or 'draw', centered on input1 as the main
        player."""
        pass

    def breed_organism_from_parents(self, organisms):
        """Given a list of organisms, return a child of all of them by
        averaging their action distributions."""
        pass

    def get_strongest_organisms(self, organisms):
        """Return a list of the strongest organisms. Must be at least one, but
        could be more."""
        pass
