def clamp_health(value, maximum=100):
    """Clamp a health value to the range [0, maximum]."""
    if type(value) is not int or type(maximum) is not int:
        raise TypeError("Both value and maximum must be exact integers.")
    if maximum <= 0:
        raise ValueError("maximum must be greater than 0.")
    if value < 0:
        return 0
    if value > maximum:
        return maximum
    return value
