# https://leetcode.com/problems/reverse-words-in-a-string-iii/


# Better to use 2 pointers, refactor in future
input = "Let's take LeetCode contest"

def reverseWords(s: str) -> str:
    ans = ""
    words = s.split(' ')
    for word in words:
        for i in range(len(word) - 1 , -1, -1):
            ans += word[i]
        ans += " "

    ans = ans[:-1]
    return ans


print(reverseWords(input))