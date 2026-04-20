# 010 — Missing Number

# Given array containing n distinct numbers in range [0,n], return missing one.

# Example

# Input: [3,0,1]
# Output: 2

input_nums = [3, 0, 1]
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum
print(missing_number(input_nums))  # Output: 2