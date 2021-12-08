# zad2
def print_names(names: list) -> None:
    for name in names:
        print(name)


print_names(names=['imie1', 'imie2', 'imie3', 'imie4', 'imie5'])

# b1)


def mul_2(numbers_1: list) -> list:
    lista_1 = []
    for number_1 in numbers_1:
        lista_1.append(number_1 * 2)
    return lista_1


print(mul_2(numbers_1=[1, 2, 3, 4, 5]))

# b1)


def multiply_2b(numbers_2: list) -> list:
    return [number_2 * 2 for number_2 in numbers_2]


print(multiply_2b(numbers_2=[1, 2, 3, 4, 5]))

# c

numbers_3 = range(1, 10)
for number_3 in numbers_3:
    if number_3 % 2 == 0:
        print(number_3)

# d) co drugi zaczynajac od 1

numbers = range(1, 10)
# print(list(numbers[::2]))

for i, number in enumerate(numbers):
    if i % 2 == 0:
        print(number)
