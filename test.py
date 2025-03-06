total_number = 0
rings = input("how many rings --- ")
for number in rings:
    int_number = int(number)
    total_number = total_number + int_number
            
    if total_number % 3 == 0:
        result = "It is NOT a prime number" 
    else:
        result = "It is a prime number"
residuo = 108 % 3
print(result)
print(f"resultado residuo --- {residuo}")