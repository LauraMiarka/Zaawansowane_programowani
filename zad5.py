# zad5

def lista(x: list, y: int) -> bool:
    if y in x:
        return True
    else:
        return False


wynik = lista([2, 3, 4], 5)

print(wynik)
