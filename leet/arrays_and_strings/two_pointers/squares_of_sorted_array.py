from typing import List


input = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]

range(len(input) -1, -1, -1 )

def sortedSquares(A: List[int]) -> List[int]:
    return_array = [0] * len(A)
    write_pointer = len(A) - 1
    left_read_pointer = 0
    right_read_pointer = len(A) - 1
    left_square = A[left_read_pointer] ** 2
    right_square = A[right_read_pointer] ** 2
    while write_pointer >= 0:
        if left_square > right_square:
            return_array[write_pointer] = left_square
            left_read_pointer += 1
            left_square = A[left_read_pointer] ** 2
        else:
            return_array[write_pointer] = right_square
            right_read_pointer -= 1
            right_square = A[right_read_pointer] ** 2
        write_pointer -= 1
    return return_array

print(sortedSquares(input))
        
