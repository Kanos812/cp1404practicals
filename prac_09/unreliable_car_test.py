"""
CP1404 Practical 09
Unreliable Car Test
Harrison O'Kane
21/11/2024
"""

from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar(name="Tesla Model F", fuel=100, reliability=0) #Define car attributes
my_unreliable_car.drive(40) #Drive 40km

print(my_unreliable_car) #Print car attributes

