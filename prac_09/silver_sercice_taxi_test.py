"""
CP1404 Practical 09
Silver Service Taxi Test
Harrison O'Kane
21/11/2024
"""

from silver_service_taxi import SilverServiceTaxi

hummer_taxi = SilverServiceTaxi("Hummer", fuel=200, fanciness=2)
hummer_taxi.drive(18)
print(hummer_taxi)
print(f"Your fare is ${hummer_taxi.get_fare()}")