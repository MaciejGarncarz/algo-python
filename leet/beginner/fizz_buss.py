n1 = 3
n2 = 5
n3 = 15

def fizzBuzz(n: int) -> list[str]:
    result: list[str] = []
    for x in range(1, n + 1):
        currentAnswer = ""
        if x % 3 == 0:
            currentAnswer += "Fizz"
        if x % 5 == 0:
            currentAnswer += "Buzz"
        if currentAnswer == "":
            currentAnswer = str(x)

        result.append(currentAnswer)
    
    return result


print(fizzBuzz(n3))