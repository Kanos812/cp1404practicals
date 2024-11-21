"""
taxi_test.py
"""

from prac_09.taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100) #Define taxi attributes
my_taxi.drive(40) #Drive 40km

print(my_taxi) #Print taxi attributes
print(f"Current fare: ${my_taxi.get_fare():.2f}") #Display the current calculated fare

my_taxi.start_fare() #Restarting meter
my_taxi.drive(100)

print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}") #Print details again after second trip