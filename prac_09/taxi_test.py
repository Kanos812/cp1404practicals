from prac_09.taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100, price_per_km=1.23)
my_taxi.drive(40)

print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")