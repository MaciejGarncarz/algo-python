# https://leetcode.com/problems/generate-parentheses/description/

from typing import List


def generateParenthesis(n: int) -> List[str]:
    answer = []

    def backtrack(curr: List[str], leftCount: int, rightCount: int):
        if len(curr) == n * 2:
            answer.append("".join(curr)) 
            return
        
    # zostawiam na pozniej nie ogarnelem tego wogole


    backtrack([], 0, 0)
    return answer


print(generateParenthesis(3))