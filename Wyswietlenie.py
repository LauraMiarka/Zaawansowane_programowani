from Pacjent import Pacjent
from Dieta import Dieta
from Dietetyk import Dietetyk
from Zamowienie import Zamowienie

dietetyk = Dietetyk("Janina", "Kowalska", 1, "123 456 789")
dieta = Dieta(2, 156.20, dietetyk, 1300)
pacjent = Pacjent("Laura", "Miarka", 34, dieta)

print(Zamowienie(1, pacjent, pacjent, dietetyk, dieta, dieta, dieta))
