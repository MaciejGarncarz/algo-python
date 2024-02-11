# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4664/

i_jewels = "aA"
i_stones = "aAAbbbb"

def numJewelsInStones(jewels: str, stones: str) -> int:
    jewels_set = set(jewels)
    ans = 0
    for stone in stones:
        if stone in jewels_set:
            ans += 1

    return ans


print(numJewelsInStones(i_jewels, i_stones))