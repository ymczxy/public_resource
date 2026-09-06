def clamp_health(value, maximum=100):
    """Clamp an integer health value into the range [0, maximum]."""
    if type(value) is not int or type(maximum) is not int:
        raise TypeError("value and maximum must be exact int instances")
    if maximum <= 0:
        raise ValueError("maximum must be greater than 0")
    if value < 0:
        return 0
    if value > maximum:
        return maximum
    return value
