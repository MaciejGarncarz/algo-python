# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/

from typing import List


def maxNumberOfApples(weight: List[int]) -> int:
    weight.sort()
    currentWeight = 5000
    numberOfApplesInBasket = 0

    for apple in weight:
        currentWeight -= apple

        if currentWeight < 0:
            break

        numberOfApplesInBasket += 1
    
    return numberOfApplesInBasket


weight = [988,641,984,635,461,527,491,610,274,104,348,468,220,837,126,111,536,368,89,201,589,481,849,708,258,853,563,868,92,76,566,398,272,697,584,851,302,766,88,428,276,797,460,244,950,134,838,161,15,330]
print(maxNumberOfApples(weight))
