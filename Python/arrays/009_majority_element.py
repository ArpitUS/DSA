# 009 — Majority Element

# Given array of size n, return element appearing more than n/2 times.

# Assume majority always exists.

# Example

# Input: [3,2,3]
# Output: 3

input_nums = [3, 2, 3]
def majority_element(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

print(majority_element(input_nums))  # Output: 3