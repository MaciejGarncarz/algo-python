# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4690/

input = "pwwkew"


def lengthOfLongestSubstring(s: str) -> int:
    characters_counter = dict()
    left = answer = 0 

    for right in range(len(s)):
        value = characters_counter.get(s[right], 0) + 1
        characters_counter[s[right]] = value

        while characters_counter[s[right]] > 1:
            characters_counter[s[left]] -= 1
            if characters_counter[s[left]] == 0:
                del characters_counter[s[left]]
            left += 1

        answer = max(answer, len(characters_counter))

    return answer


print(lengthOfLongestSubstring(input))