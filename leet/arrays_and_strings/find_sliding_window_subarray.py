input = [3, 1, 2, 7, 4, 2, 1, 1, 5]
output = [4, 2, 1, 1]
kInput = 8

def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans


print(find_length(input, kInput))