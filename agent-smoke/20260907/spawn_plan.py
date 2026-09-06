"""Small helpers for synthetic game spawn planning."""


def allocate_spawn_slots(counts, limit=1000):
    """Return spawn coordinates grouped by wave after validating all inputs."""
    if not isinstance(counts, list):
        raise TypeError("counts must be a list")

    for count in counts:
        if type(count) is not int:
            raise TypeError("each count must be an exact int")
        if count < 0:
            raise ValueError("counts must be non-negative")

    if type(limit) is not int:
        raise TypeError("limit must be an exact int")
    if limit < 0:
        raise ValueError("limit must be non-negative")

    if sum(counts) > limit:
        raise ValueError("total count exceeds limit")

    return [
        (wave_index, unit_index)
        for wave_index, count in enumerate(counts)
        for unit_index in range(count)
    ]
