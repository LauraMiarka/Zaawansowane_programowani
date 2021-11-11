"""
Lab_2
Zadanie_2

a) utwórz funkcje, która otrzyma w parametrze listę 5 imion, a nastepnie wyświetl każde z nich
"""

def print_names(names: list) -> None:
    for name in names:
        print(name)

print_names(names = ['imie1', 'imie2' ,'imie3' ,'imie4' ,'imie5'])

# b1)

def mul_2(numbers: list) -> list:
    lista = []
    for number in numbers:
        lista.append(number*2)
    return lista

print(mul_2(numbers = [1, 2, 3, 4, 5]))

# b1)

def multiply_2b(numbers: list) -> list:
    return [number*2 for number in numbers]

print(multiply_2b(numbers = [1, 2, 3, 4, 5]))


#c

numbers = range(1,10)
for number in numbers:
    if number%2==0:
        print(number)

#d) co drugi zaczynajac od 1

numbers = range(1,10)
#print(list(numbers[::2]))

for i, number in enumerate(numbers):
    if i%2==0:
       print(number)

