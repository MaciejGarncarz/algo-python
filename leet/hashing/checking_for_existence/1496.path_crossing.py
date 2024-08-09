# https://leetcode.com/problems/path-crossing/description/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        origin = (0, 0)
        charted = set([(0, 0)])

        directions = {"N": (0, 1), "S": (0, -1),"E": (1, 0), "W": (-1, 0)}

        for nextPath in path:
            x, y = directions[nextPath]

            currX, currY = origin
            origin = (currX + x, currY + y)

            if origin in charted:
                return True
            
            charted.add(origin)
        
        return False
    

obj = Solution()
print(obj.isPathCrossing("NESWW"))
