def average_or_none(values):
    if not values:
        return None

    return sum(values) / len(values)

