"""Small statistical helpers used in the pull request demonstrations."""

def data_range(values):
    return max(values) - min(values)

def average_or_none(values):
    if not values:
        return None

    return sum(values) / len(values)