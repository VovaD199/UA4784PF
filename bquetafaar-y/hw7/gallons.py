def zero_fuel(distance_to_pump, mpg, fuel_left):
    fuelRequired = distance_to_pump/mpg
    if fuelRequired > fuel_left:
        return False
    else:
        return True
