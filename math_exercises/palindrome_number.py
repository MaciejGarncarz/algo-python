def is_palindrome(number:int) -> bool:
    reverse = 0
    temp = number
    while temp != 0:
        last_digit = temp % 10
        reverse = reverse * 10 + last_digit
        temp = int(temp / 10)

    return number == reverse

number_input = int(input("write something  "))
print(is_palindrome(number_input))