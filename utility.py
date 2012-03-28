from random import random

def normalize_tuple(tuple_to_normalize, total = 1):
    """Take a total value and a tuple. Normalize the tuple's entries such that
    they add up to total."""
    if total == 0:
        return False

# if tuple includes negative values, remove them by subtracting the largest
# negative value
    if min(tuple_to_normalize) < 0:
        tuple_to_normalize = [element - min(tuple_to_normalize) 
            for element in tuple_to_normalize]

    current_total = sum(tuple_to_normalize)
    divisor = current_total / total
    return tuple([i/divisor for i in tuple_to_normalize])

def get_distribution_choice(distribution):
    """Given a probability distribution in the form of a tuple, return a random choice of an element (using those probabilities)."""
    random_choice = random()
    for i in range(len(distribution)):
        interval = sum(distribution[0:i+1])
        if random_choice <= interval:
            return i

