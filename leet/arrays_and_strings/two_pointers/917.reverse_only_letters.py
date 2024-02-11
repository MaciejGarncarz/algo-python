# https://leetcode.com/problems/reverse-only-letters/description/

input1 = "ab-cd"
input2 = "a-bC-dEf-ghIj"
input3 = "Test1ng-Leet=code-Q!"

def reverse_only_letters(s: str) -> str:
    left = 0
    right = len(s) - 1
    answer = list(s)

    while left < right: 
        leftValue = s[left]
        rightValue = s[right]

        if leftValue.isalpha() == False:
            left += 1
        elif rightValue.isalpha() == False:
            right -= 1
        else:
            answer[left] = rightValue
            answer[right] = leftValue
            left += 1
            right -= 1

    return "".join(answer)

print(reverse_only_letters(input3))
