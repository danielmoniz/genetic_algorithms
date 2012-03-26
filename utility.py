def normalize_tuple(tuple_to_normalize, total = 1):
    """Take a total value and a tuple. Normalize the tuple's entries such that
    they add up to total."""
    if total == 0:
        return False
    current_total = sum(tuple_to_normalize)
    divisor = current_total / total
    return tuple([i/divisor for i in tuple_to_normalize])
