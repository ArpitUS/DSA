# 004 — Maximum Subarray

# Given integer array nums, find contiguous subarray with largest sum and return its sum.

# Example

# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1]

input_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
            
    return max_sum  

print(max_subarray(input_nums))  # Output: 6