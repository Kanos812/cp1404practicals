import math

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

#Print model information with year number, name and rounded up cost
cost = round(cost)
print(f"{year} {name} for about ${cost:,}!")

#Print power values
for current_power_value in range(11):
    print(f"2 ^{current_power_value:2} is {2 ** current_power_value:4}")
