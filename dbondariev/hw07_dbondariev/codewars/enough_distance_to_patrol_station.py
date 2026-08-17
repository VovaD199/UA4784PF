zero_fuel = lambda distance_to_pump, mpg, fuel_left: fuel_left * mpg >= distance_to_pump

print(zero_fuel(5, 5, 5))
print(zero_fuel(100, 50, 1))