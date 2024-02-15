# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4612/

from typing import List


input1 = [4,1,2]
input2 = [1,3,4,2]


# zrobic hashmape
# iterowac po nums1
# znalesc element w hashmapie i jego index
# od tego indexu + 1 zaczac iterowac po num2
# jesli element znajdzie sie wiekszy to dodac do answer
# jesli nic sie nie znajdzie to -1


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    answer = []
    hashMap = {}

    for index, x in enumerate(nums2):
        hashMap[x] = index

    for x in nums1:
        wasAppended = False
        elementValue = hashMap[x]
        for index in range(elementValue, len(nums2), 1):
            value = nums2[index]
            if value > x:
                answer.append(value)
                wasAppended = True
                break
        if wasAppended == False:
            answer.append(-1)
    return answer


result = next_greater_element(input1, input2)
print('test')