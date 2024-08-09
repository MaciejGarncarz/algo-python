from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        MOD = 10**9 + 7
        start = 0
        end = n

        while start < end:
            subArray = nums[start:end]
            curr = 0
            for x in subArray:
                curr += x
                sums.append(curr)
            start += 1
        
        sums.sort()

        answer = 0

        for x in range(left-1, right):
            answer = (answer + sums[x]) % MOD
        
        return answer
            


obj = Solution()
obj.rangeSum([1,2,3,4], 4, 1, 5)



        