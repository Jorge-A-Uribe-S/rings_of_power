def prime():
    result = "It is a prime number"
    return result

def not_prime():
    result = "It is NOT a primer number"
    return result

def prime_number(rings):
    total_number = 0
    cyphers = len(rings)
    if rings == "2" or rings == "5" or rings == "3" or rings == "7":
        result = prime()

    elif rings == "0" or rings == "1" or rings == "4" or rings == "6" or rings == "8" or rings == "9":
        result = not_prime()
    
    elif cyphers > 1:
        if rings[cyphers - 1] == "0" or rings[cyphers - 1] == "6" or rings[cyphers - 1] == "2" or rings[cyphers - 1] == "4" or rings[cyphers - 1] == "5" or rings[cyphers - 1] == "8" :
            result = not_prime()
        else:
            total_number = 0
            for number in rings:
                int_number = int(number)
                total_number = total_number + int_number
            
            if total_number % 3 == 0:
                result = not_prime() 
            else:
                result = prime()
            
    return result
        
    

