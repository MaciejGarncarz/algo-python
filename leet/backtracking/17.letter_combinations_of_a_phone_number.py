#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List


def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    digitsList = list(digits)
    answer = []

    phone =  {
            '2' : 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
    def backtrack(curr: List[str], i: int):
        if len(curr) == len(digitsList):
            answer.append("".join(curr))
            return


        digit = digitsList[i]
        letters = phone[digit]
        for letter in letters:
            curr.append(letter)
            backtrack(curr, i + 1)
            curr.pop()


    backtrack([], 0)
    return answer


digits = "2"
print(letterCombinations(digits))



