def find_factorial(number: int) -> int: #better solution in terms of algo
    result = 1
    for n in range(1, number + 1):
        result = result * n
    return result

def find_factorial_recursive(number: int) -> int:
    if number == 0:
        return 1
    
    return number * (find_factorial(number - 1))



number = int(input("provide input:  "))
print(f"Loop method: {find_factorial(number)}")
print(f"Recursive method: {find_factorial_recursive(number)}")
