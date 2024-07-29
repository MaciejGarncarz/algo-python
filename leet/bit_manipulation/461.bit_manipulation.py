class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance
    

obj = Solution()
print(obj.hammingDistance(1, 4))
