# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/

from typing import List


def numsSameConsecDiff(n: int, k: int) -> List[int]:
    answer = []

    def backtrack(curr: List[str], index: int, indexToCheck: int):
        if len(curr) == n:
            answer.append(int("".join(curr)))
            return

        for number in range(index, 10):
            if len(curr) == 0:
                if number != 0:
                    curr.append(str(number))
                    backtrack(curr, index, indexToCheck)
                    curr.pop()
            else:
                currNumber = curr[indexToCheck]

                if(abs(int(currNumber) - number)) == k:
                    curr.append(str(number))
                    backtrack(curr, index, indexToCheck + 1)
                    curr.pop()
    
    backtrack([], 0, 0)
    return answer


n = 2
k = 1
print(numsSameConsecDiff(n, k))