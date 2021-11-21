#zad6

def merge(x:list, y:list) -> list:
    list_3 = set(x+y)
    list_power = [a**3 for a in list_3]
    return list_power

wynik = merge([1,2,3,4],[2,3,4,5])

print(wynik)