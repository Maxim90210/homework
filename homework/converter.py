def cm_to_inches(length_cm):
    """Converts length from centimeters to inches."""
    if length_cm < 0:
        return -length_cm
    else:
        return round(length_cm / 2.54, 2)