"""
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
 """
from defs import prime_number, check_if_negative_number

sauron = 0
elfs = 0
dwarfs = 0
men = 0

total_number_of_rings = input("How many rings are you going to distribute? ---  ")
total_number_of_rings_int = int(total_number_of_rings)

for i in range(-(total_number_of_rings_int), 1):
    positive_number = -(i)
    positive_number = str(positive_number)
    if prime_number(positive_number) == True:
        dwarfs = positive_number
        dwarfs = int(dwarfs)
        break
    else:
        pass
total_number_of_rings_int = total_number_of_rings_int - dwarfs


if total_number_of_rings_int <= 0:
    print("The rest of the rings cannot be distributed, next time try with another number of rings")
else:
    print(f"Rings for Dwarfs ----- {dwarfs}")
    print(f"Rings left to distribute {total_number_of_rings_int}")

    sauron = (total_number_of_rings_int - (total_number_of_rings_int - 1))
    total_number_of_rings_int = total_number_of_rings_int - sauron

    print(f"Rings for Sauron ----- {sauron}")
    print(f"Rings left to distribute {total_number_of_rings_int}")
"""
for i in range(total_number_of_rings_int, 0, -1):
    i = str(i)
    prime_result = prime_number(i)
    if prime_result == True:
        print(f"{i} es el número primo más alto en esta serie de números")
        break
    else: 
        pass






sauron = (total_number_of_rings_int - (total_number_of_rings_int - 1))
total_number_of_rings_int = total_number_of_rings_int - sauron
if total_number_of_rings_int % 2 == 0:
    men = total_number_of_rings_int / 2
    total_number_of_rings_int = total_number_of_rings_int - men
else:
    men = (total_number_of_rings_int - 1) / 2
    total_number_of_rings_int = total_number_of_rings_int - men

if (total_number_of_rings_int / 2) % 2 == 1:
    elfs = total_number_of_rings_int /2
    total_number_of_rings_int = total_number_of_rings_int - elfs
else: 
    elfs = (total_number_of_rings_int - 1) /2
    total_number_of_rings_int = total_number_of_rings_int - elfs

total_number_of_rings = str(total_number_of_rings_int)
prime_result = prime_number(total_number_of_rings)

print(f"Rings for Sauron ----- {sauron}")
print(f"Rings for Men ----- {men}")
print(f"Rings for Elfs ----- {elfs}")
print(f"Rings for Dwarfs ----- {dwarfs}")
print(prime_result, total_number_of_rings_int)"
"""

