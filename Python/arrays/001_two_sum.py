# 001 — Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Each input has exactly one solution, and you may not use the same element twice.

# Example:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

array = [2, 7, 11, 15]
target = 9  

def two_sum(nums, target):
    num_to_index = {}
    
    for i, num in enumerate(nums):
        compliment = target - num
        
        if compliment in num_to_index:
            return [num_to_index[compliment], i]
        num_to_index[num] = i
        
    return []  # Return an empty list if no solution is found

result = two_sum(array, target)
print(result)  # Output: [0, 1]