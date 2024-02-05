import timeit
import math

def find_factorial(number: int) -> int:
    # factorial exists only for n>=0
    if (number < 0):
        return 0
  
    # base case
    if (number <= 1):
        return 1
  
    # else iterate through n and
    # calculate the value
    digits = 0
    for i in range(2, number + 1):
        digits += math.log10(i)
  
    return math.floor(digits) + 1




# result = timeit.timeit(lambda: find_factorial(8428), number=188)
# print(f"time result:{result}")
print(f"Factorial result: {find_factorial(5)}")
