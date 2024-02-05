import math

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    
    for x in range(3, int(math.sqrt(number)) + 1, 2):
        if number % x == 0:
            return False
    return True


# number_input = int(input("write something  "))
print(is_prime(15));
