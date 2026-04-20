# 005 — Move Zeroes

# Move all 0s to end while maintaining relative order of non-zero elements.

# Do it in-place.

# Example

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

input_nums = [0, 1, 0, 3, 12]

def move_zeroes(nums):
    last_non_zero = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
            
    return nums

print(move_zeroes(input_nums))  # Output: [1,3,12,0,0]