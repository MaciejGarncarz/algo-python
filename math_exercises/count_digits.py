def count_digits(number: int) -> int:
    if number == 0:
        return 1
    current_count = 0
    while number > 0:
        number = int(number / 10) 
        current_count = current_count + 1

    return current_count



number = int(input("provide input:  "))
print(count_digits(number))