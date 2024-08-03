# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/?envType=daily-question&envId=2024-08-03

# This is very weird question it asks to reverse subarrays but in reality you can sort and compare
# Also common approach is just to count keys if they arrays are the same. 

from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        right = 0
        
        for index in range(len(arr)): # O(n)
            if target[index] != arr[index]:
                while right != len(arr) and arr[right] != target[index]:
                    right += 1
                if right == len(arr):
                    return False
                
                arr[index:right+1] = arr[index:right+1][::-1]

                right = index
            right += 1

        return True
    


obj = Solution()
obj.canBeEqual([1,2,3,4], [2,4,1,3])


# class Solution2:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         # Sort both arrays and compare
#         return sorted(target) == sorted(arr)