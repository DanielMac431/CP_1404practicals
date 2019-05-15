from prac_08.silver_service_taxi import SilverServiceTaxi


limo = SilverServiceTaxi('Limo', 100, 2)
limo.drive(18)
print(limo)
print(limo.get_fare())