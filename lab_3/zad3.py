#zad3

def parzysta(x) -> bool:
    if x%2==0:
        return True
    else:
        return False

wynik = parzysta(5)

if wynik == True:
    print ("Liczba parzysta")
else:
    print("Liczba nieparzysta")

