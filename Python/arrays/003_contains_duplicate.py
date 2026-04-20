# 003 — Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice, else return false.

# Example

# Input: [1,2,3,1]
# Output: true

input_nums = [1, 2, 3, 1]

def contains_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
        
    return False
print(contains_duplicate(input_nums))  # Output: true