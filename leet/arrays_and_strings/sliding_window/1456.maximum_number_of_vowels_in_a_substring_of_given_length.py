# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

input = "leetcode"
target_length = 3


def max_vowels(s: str, k: int) -> int:
    left = right = curr = answer = 0
    VOVELS = ['a', 'e', 'i', 'o', 'u']

    for x in range(0, k):
        current_value = s[x]
        if current_value in VOVELS:
            curr += 1
        
        right += 1
        
            
    answer = curr
    
    while right < len(s):
        if s[right] in VOVELS:
            curr += 1

        if s[left] in VOVELS:
            curr -= 1

        right += 1
        left += 1
        
        answer = max(answer, curr)
        
    
    return answer
    

print(max_vowels(input, target_length))


# 