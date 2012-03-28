#!/usr/bin/env python
# Import the necessary files here, depending on your game.
# It is vital that they are represented as 'Organism' and 'Game'.
from rps_organism import SubOrganism as Organism
from game import RockPaperScissors as Game

import utility
import sys

MAJOR_LINE_BREAK = "---------------------------------------------------"
MINOR_LINE_BREAK = "--------------------------"
print MAJOR_LINE_BREAK
try:
    POPULATION = int(sys.argv[1])
    NUM_GAME_TURNS = int(sys.argv[2])
    print "Population:", POPULATION, ", number of game turns:", NUM_GAME_TURNS
except IndexError:
# Default population and game turn settings
    POPULATION = 100
    NUM_GAME_TURNS = 20
    print "Using default population (" + str(POPULATION) + ") and number of game turns (" + str(NUM_GAME_TURNS) + ")."

# ==========================================================
# create single game instance
game = Game(POPULATION, NUM_GAME_TURNS)

print MINOR_LINE_BREAK
chromosones = game.generate_initial_population()
# used for debugging. And watching organism changes over generations.
"""for chrom in chromosones:
    print chrom
    print chrom.rps
    """

organisms = []
user_rps = utility.normalize_tuple((0.2, 0.5, 0.3))
print "User distribution:", user_rps

# Loop through each game turn. Select a random user choice out of the provided
# distribution each time.
for i in range(NUM_GAME_TURNS):
    user_index_selection = utility.get_distribution_choice(user_rps)
    user_action = game.actions[user_index_selection]
    organisms = game.run_game_turn(chromosones, user_action)

#print get_organism_stats(organisms)
organism_list = []
for chrom in organisms:
    organism_list.append([chrom.hit_points, [round(rps_element, 2) for rps_element in chrom.rps]])

organism_list = sorted(organism_list)
print "Top 5 (or less) organisms, sorted by hit points:"
for org in reversed(organism_list[-5:]):
    print org

strongest_organisms = game.get_strongest_organisms(organisms)

super_child_organism = game.breed_organism_from_parents(strongest_organisms)
print "Latest super child organism:", [round(rps_element, 2) for rps_element in super_child_organism.rps]
print MAJOR_LINE_BREAK
