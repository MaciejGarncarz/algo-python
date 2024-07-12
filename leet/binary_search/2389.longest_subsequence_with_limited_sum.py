# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

from typing import List


def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    answer = []
    nums.sort()
    prefix = [nums[0]]


    for index in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[index]) 

    for query in queries:
        left = 0
        right = len(prefix) -1

        while left < right:
            mid = (left + right) // 2
            if prefix[mid] == query:
                left = mid
                break
            elif prefix[mid] >= query:
                right = mid - 1
            else:
                left = mid + 1

        value = prefix[left]
        if value <= query:
            answer.append(left + 1)
        else:
            answer.append(left)

    return answer        

nums = [4,5,2,1]
queries = [3,10,21]      

print(answerQueries(nums,queries))